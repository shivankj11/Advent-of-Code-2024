from collections import *
from functools import *
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as sw
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

def find_seq(A, seq):
    """ Returns indices of seq in A"""
    return np.where(reduce(op.and_, ((np.concatenate([(A == s)[i:], np.zeros(i, dtype=np.uint8)],dtype=np.uint8)) for i,s in enumerate(seq))))[0]

def kosaraju(adj_list : Dict[Any, List[Any]])-> List[List[Any]]:
    """ Returns list of strongly connected components for a directed graph
        
        PARAMETERS:
            adj_list : Dictionary mapping Nodes -> List of neighboring nodes
        
        RETURNS:
            List of strongly connected components (Lists of nodes)
    """

    # DFS for in-order traversal
    visited = set()
    stack = deque(adj_list.keys())

    L = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            L.append(v)
            stack.extend(adj_list[v])
    
    # Get reverse order traversal
    L = L[::-1]

    # Find SCCS
    def assign(v, group : List, assigned : Set):
        if v in assigned:
            return group, assigned

        assigned.add(v)
        group.append(v)
        for u in adj_list[v]:
            if u not in assigned:
                group.append(u)
                assigned.add(u)
            group, assigned = assign(u, group, assigned)
        
        return group, assigned

    sccs = []
    assigned = set()
    for v in L:
        group, assigned = assign(v, [], assigned)
        sccs.append(group)
    
    return [scc for scc in sccs if scc]

def bors_kerbosch(R, P, X, G, C):
        """ Returns maximal cliques of G """
        if len(P) == 0 and len(X) == 0:
            if len(R) > 2:
                C.append(sorted(R))            
            return

        pivot = max(P.union(X))
        for v in P.difference(G[pivot]):
            bors_kerbosch(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
            P.remove(v)
            X.add(v)

def max_clique(adj_list : Dict[Any, List[Any]])-> List[List[Any]]:
    """ Returns largest clique of a graph

        PARAMETERS:
            adj_list : Non-empty dictionary mapping Nodes -> List of neighboring nodes
        
        RETURNS:
           Clique of maximum size of clique in the graph
    """
    cliques = []
    bors_kerbosch(set([]), set(adj_list.keys()), set([]), adj_list, cliques)
    
    cliques.sort(key=len)
    return cliques[-1]