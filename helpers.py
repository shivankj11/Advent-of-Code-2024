from collections import *
from functools import *
import numpy as np
from typing import *
import itertools as it
import re
import operator as op
from abc import *

npa = np.asarray

lmap = lambda f,L : list(map(f, L))

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

class search(ABC):

    def __init__(self, neighbor_fn):
        self.nfn = neighbor_fn
    
    @abstractmethod
    def find(self, start, target):
        pass