import numpy as np
from .model import TopsisModel
from typing import Tuple


class Topsis:
    """
    Apply TOPSIS method to calculate similarity scores
    and rankings based on given features

    :param matrix: numpy array to apply TOPSIS method
    :param criteria: criteria to use to min-max optimization
    :param weights: weights to use to calculate the weighted matrix
    """

    def __init__(
        self,
        matrix: np.ndarray,
        criteria: list,
        weights: list = None
    ) -> None:
        self._matrix = matrix
        self._criteria = criteria
        self._weights = weights

        self._height = matrix.shape[0]
        self._width = matrix.shape[1]

    def _check_types(self) -> None:
        """
        Check types of given parameters
        """
        if not isinstance(self._matrix, np.ndarray):
            raise TypeError('Invalid data type for matrix')

        if not isinstance(self._criteria, list):
            raise TypeError('Invalid data type for criteria')

        if not isinstance(self._weights, list):
            raise Exception('Invalid data type for weights')

    def normalize(self) -> np.ndarray:
        """
        Normalize the values with the vector normalization method
        in step 2 of the TOPSIS

        :return: normalized matrix
        """
        # calculate the square sum of the squares
        # of all the values in the column
        sqrt_sum = (self._matrix ** 2).sum(axis=0)

        # divide all values by the square root of the sums
        return self._matrix / sqrt_sum ** 0.5

    def add_weights(self, arr: np.ndarray) -> np.ndarray:
        """
        Calculate the weighted normalised decision matrix
        in step 3 of the TOPSIS

        :param arr: normalized matrix
        :return: weighted normalised decision matrix
        """
        return arr * self._weights

    def find_alternatives(
        self,
        arr: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Determine the worst alternative and the best alternative
        in step 4 of the TOPSIS

        :param arr: weighted normalised decision matrix
        :return: worst alternative and the best alternative
        """
        # create zero matrices
        worst = np.zeros(self._width)
        best = np.zeros(self._width)

        # calculate worst and best alternatives by criteria
        for i in range(self._width):
            if self._criteria[i]:
                worst[i] = min(arr[:, i])
                best[i] = max(arr[:, i])
                continue

            worst[i] = max(arr[:, i])
            best[i] = min(arr[:, i])

        return worst, best

    def find_distances(
        self,
        arr: np.ndarray,
        worst: np.ndarray,
        best: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate the L2-distance between the target alternative
        and the worst condition and the distance between the alternative
        and the best condition in step 5 of the TOPSIS

        :param arr: weighted normalised decision matrix
        :param worst: worst alternative
        :param best: best alternative
        :return: worst distance and the best distance
        """
        # calculate distances between weighted matrix and alternatives
        worst_dist = np.sqrt(np.sum((arr - worst) ** 2, axis=1))
        best_dist = np.sqrt(np.sum((arr - best) ** 2, axis=1))

        return worst_dist, best_dist

    def find_similarities(
        self,
        worst_dist: np.ndarray,
        best_dist: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate the similarity to the worst and best condition
        in step 6 of the TOPSIS

        :param worst_dist: worst distance
        :param best_distance: best distance
        :return: worst similarity and the best similarity
        """
        # calculate similarity to the worst condition
        worst_sim = worst_dist / (worst_dist + best_dist)

        # calculate similarity to the best condition
        best_sim = best_dist / (worst_dist + best_dist)

        return worst_sim, best_sim

    def ranking(self, similarities: np.ndarray) -> list:
        """
        Assign ranks by similarities

        :param similarities: worst similarity or best similarity
        """
        return [i + 1 for i in similarities.argsort()]

    def calculate(self) -> TopsisModel:
        """
        Calculate all metrics to TOPSIS

        :return: base metrics with custom TopsisModel data type
        """
        # if no weights are used for observations
        if self._weights is None:
            self._weights = [1] * self._weights

        # check the type of given parameters
        self._check_types()

        # normalize matrix
        normalized = self.normalize()

        # create weighted normalised decision matrix
        weighted = self.add_weights(normalized)

        # find worst alternative and the best alternative
        worst, best = self.find_alternatives(weighted)

        # find worst distance and the best distance
        worst_dist, best_dist = self.find_distances(
            weighted,
            worst,
            best
        )

        # find worst similarities and the best similarities
        worst_sim, best_sim = self.find_similarities(
            worst_dist,
            best_dist
        )

        # find worst ranks and the best ranks
        worst_ranks = self.ranking(worst_sim)
        best_ranks = self.ranking(worst_sim)

        model = TopsisModel(
            best_ranks=best_ranks,
            best_similarities=best_sim,
            worst_ranks=worst_ranks,
            worst_similarities=worst_sim
        )

        return model
