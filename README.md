# ISTOP
TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) implementation in python

Please checkout this [link](https://en.wikipedia.org/wiki/TOPSIS#TOPSIS_method) to see more details
about TOPSIS steps. 

## Install

You can install the latest release,

```zsh
$ pip install istop
```

## Usage

```python
>>> import numpy as np
>>> from istop import Topsis

>>> evaluation_matrix = np.array([
...     [1, 2, 3, 4],
...     [4, 3, 2, 1],
...     [3, 3, 3, 3],
...     [4, 4, 4, 4],
...     [1, 2, 4, 4]
... ])
>>> criteria = [False, True, True, True]
>>> weights = [5, 5, 9, 0]

>>> topsis = Topsis(
...     matrix=evaluation_matrix,
...     criteria=criteria,
...     weights=weights
... )
>>> result = topsis.calculate()
>>> print(result.best_ranks)
[2, 3, 4, 1, 5]
>> print(result.worst_similarities)
[0.56842726 0.18322884 0.43760627 0.55861195 0.68474356]
```

The **_weights_** parameter is optional. 
If you don't send it, the default value for each attribute will be 1.

## Contribution

Please check to the pylint and flake8 steps in workflow before contribution.
