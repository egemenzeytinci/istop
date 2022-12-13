import numpy as np


class TopsisModel:
    """
    Generate topsis result object from given parameters

    :param best_ranks: best rank calculated using best similarities
    :param best_similarities: similarity calculated using best distances
    :param bad_ranks: best rank calculated using worst similarities
    :param worst_similarities: similarity calculated using worst distances
    """

    def __init__(
        self,
        best_ranks: list,
        best_similarities: np.ndarray,
        worst_ranks: list,
        worst_similarities: np.ndarray
    ) -> None:
        self.best_ranks = best_ranks
        self.best_similarities = best_similarities
        self.worst_ranks = worst_ranks
        self.worst_similarities = worst_similarities

    def __str__(self) -> str:
        """
        Nicely printable string representation of an object

        :return: content as text
        """
        str_val = ''

        for k in vars(self):
            str_val += f'{k}={getattr(self, k)}\n'

        return str_val[:-1]

    def __repr__(self) -> str:
        """
        Represent class content

        :return: content as text
        """
        rep = {}

        for k in vars(self):
            rep[k] = getattr(self, k)

        return str(rep)
