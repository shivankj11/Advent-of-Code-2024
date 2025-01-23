from helpers import *

with open('day7_input.txt', 'r') as f:
    text = f.read().strip()

eqns_str = [line.split(': ') for line in text.splitlines()]
eqns = [[int(x), lmap(int, y.split())] for x,y in eqns_str]

# pt1
def reduce_ns(ns, ops):
    v = ns[0]
    for n, op in zip(ns[1:], ops):
        if op:
            v *= n
        else:
            v += n
    return v

def ct_achievable(eqns, reduce_fn, n_ops=2):
    ''' Bruteforce operation permutations '''
    tot = 0
    for goal, ns in eqns:
        for ops in mesh(*([n_ops] * (len(ns) - 1))):
            if reduce_fn(ns, ops) == goal:
                tot += goal
                break
    return tot

print('Part 1:', ct_achievable(eqns, reduce_ns))

# pt2
def reduce_ns2(ns, ops):
    v = ns[0]
    for n, op in zip(ns[1:], ops):
        if op == 2:
            v *= n
        elif op:
            v += n
        else:
            v = int(str(v) + str(n))
    return v

print('Part 2:', ct_achievable(eqns, reduce_ns2, n_ops=3))