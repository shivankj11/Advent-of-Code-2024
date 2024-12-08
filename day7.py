from helpers import *

with open('day7_input.txt', 'r') as f:
    text = f.read().strip()

eqns_str = [line.split(': ') for line in text.split('\n')]
eqns = [[int(x), lmap(int, y.split(' '))] for x,y in eqns_str]

# pt1
def reduce_ns(ns, ops):
    v = ns[0]
    for n, op in zip(ns[1:], ops):
        if op:
            v *= n
        else:
            v += n
    return v

def works(goal, ns, ops, i) -> bool:
    print(f'Operators: {lmap(lambda x : 'x' if x == 1 else "+", ops)}')
    if reduce_ns(ns, ops) == goal:
        return True
    if i >= len(ops):
        return False
    if works(goal, ns, ops, i+1):
        return True
    ops_2 = ops.copy()
    ops_2[i] = 1
    return works(goal, ns, ops_2, i+1)

def ct_achievable(eqns, reduce_fn, n_ops=2):
    tot = 0
    for goal, ns in eqns:
        # call fn to backtrack on changing + to *
        # ops = np.zeros(len(ns) - 1, dtype=int)
        # if works(goal, ns, ops, 0):
        #     tot += goal
        for ops in mesh(*([n_ops] * (len(ns) - 1))):
            if reduce_fn(ns, ops) == goal:
                tot += goal
                break

    return tot

print(ct_achievable(eqns, reduce_ns))

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

print(ct_achievable(eqns, reduce_ns2, n_ops=3))