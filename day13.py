from helpers import *

with open('day13_input.txt', 'r') as f:
    text = f.read()

text = text.strip().split('\n\n')
machines = []
for machine in text:
    a, b, prize = machine.split('\n')
    a_coord = a[12:].split(', Y+')
    b_coord = b[12:].split(', Y+')
    p_coord = prize[9:].split(', Y=')
    machines.append(lmap(partial(lmap, int), (a_coord, b_coord, p_coord)))

# pt1
button_pushes = sorted(list(mesh(101, 101)), key=lambda x : 3 * x[0] + x[1])
tokens = 0
for a, b, p in machines:
    for pusha, pushb in button_pushes:
        if (pusha * a[0] + pushb * b[0] == p[0] and
            pusha * a[1] + pushb * b[1] == p[1]):
            tokens += 3 * pusha + pushb
            break

print(tokens)

# pt2
from scipy.optimize import milp, LinearConstraint
tokens2 = 0
for a, b, p in machines:
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    prize = npa(p)
    prize += 10000000000000
    A = npa([[ax, bx], [ay, by]])
    cons = LinearConstraint(A, lb=prize-1e-2, ub=prize+1e-2) # +- for numerical inaccuracy w large nums
    opt = milp(c=[3, 1], integrality=[1,1], constraints=cons)

    if opt.success:
        pusha, pushb = opt.x
        pusha = int(pusha)
        pushb = int(pushb)
        if pusha * ax + pushb * bx == prize[0] and pusha * ay + pushb * by == prize[1]:
            tokens2 += pusha * 3 + pushb
            assert(pusha * 3 + pushb == opt.fun)

print(tokens2)