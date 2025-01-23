from helpers import *

with open('day13_input.txt', 'r') as f:
    text = f.read().strip()

machines = []
for machine in text.split('\n\n'):
    a, b, prize = machine.splitlines()
    a_coord = a[12:].split(', Y+')
    b_coord = b[12:].split(', Y+')
    p_coord = prize[9:].split(', Y=')
    machines.append([lmap(int, pt) for pt in (a_coord, b_coord, p_coord)])

# pt1
button_pushes = sorted(list(mesh(101, 101)), key=lambda x : 3 * x[0] + x[1])
tokens = 0
for a, b, p in machines:
    for pusha, pushb in button_pushes:
        if (pusha * a[0] + pushb * b[0] == p[0] and
            pusha * a[1] + pushb * b[1] == p[1]):
            tokens += 3 * pusha + pushb
            break

print('Part 1:', tokens)

# pt2
from scipy.optimize import milp, LinearConstraint
tokens2 = 0
for a, b, p in machines:
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    prize = npa(p)
    prize += 10000000000000
    A = npa([[ax, bx], [ay, by]])
    # +-.01 for numerical inaccuracy w large nums
    cons = LinearConstraint(A, lb=prize-0.01, ub=prize+0.01)
    opt = milp(c=[3, 1], integrality=[1,1], constraints=cons)
    if opt.success:
        tokens2 += int(opt.fun)

print('Part 2:', tokens2)