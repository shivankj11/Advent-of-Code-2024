from collections import *
from functools import *
import numpy as np
from typing import *
import itertools as it
import re
import operator as op
from abc import *
from heapq import *
from copy import deepcopy
from contextlib import contextmanager
import sys, os

npa = np.asarray

lmap = lambda f,L : list(map(f, L))

identity = lambda x : x

mesh = lambda *a : it.product(*map(range, a))

def median(L : List[Any]) -> Any:
    if not L:
        return None
    if len(L) % 2 == 0:
        return (L[len(L) // 2] + L[len(L) // 2 - 1]) / 2
    return L[len(L) // 2]

def grid_neighbors(pt):
    x, y = pt
    return [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]

def arr_bounds(arr : np.ndarray):
    return set(mesh(*arr.shape))

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout