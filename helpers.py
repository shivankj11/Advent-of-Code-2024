from collections import *
from functools import *
import numpy as np
from typing import *
import itertools as it
import re
import operator

npa = np.asarray

lmap = lambda f,L : list(map(f, L))

mesh = lambda *a : it.product(*map(range, a))

def median(L : List[Any]) -> Any:
    if not L:
        return None
    if len(L) % 2 == 0:
        return (L[len(L) // 2] + L[len(L) // 2 - 1]) / 2
    return L[len(L) // 2]