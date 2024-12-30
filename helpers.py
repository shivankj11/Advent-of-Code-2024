from collections import *
from functools import *
import numpy as np
from typing import *
import itertools as it
import time
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

def arr_bounds(arr : np.ndarray) -> Set[Tuple]:
    return set(mesh(*arr.shape))

def arr_border_2d(arr : np.ndarray) -> Set[Tuple]:
    rows, cols = arr.shape
    f = lambda pt : 0 < pt[0] < rows-1 and 0 < pt[1] < cols-1
    return set(it.filterfalse(f, arr_bounds(arr)))

def arr_find(arr : np.ndarray) -> Callable[Any, Any]:
    def find(e):
        return tuple(npa(np.where(arr == e)).T[0])
    return find

def grid_step(x : int, y : int, direction : int):
    """ Direction 0 = E, 1 = S, 2 = W, 3 = N """
    if direction == 0:
        return (x, y+1)
    elif direction == 1:
        return (x+1, y)
    elif direction == 2:
        return (x, y-1)
    else:
        return (x-1, y)

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def np_search_sequence(a, seq):
    return np.where(reduce(op.and_, ((np.concatenate([(a == s)[i:], np.zeros(i, dtype=np.uint8)],dtype=np.uint8)) for i,s in enumerate(seq))))[0]
