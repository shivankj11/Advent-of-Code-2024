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
import pulp
tokens2 = 0
for a, b, p in machines:
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    prize = [(p[0] + 10000000000000), (p[1] + 10000000000000)]

    m = pulp.LpProblem("Wedding Seating Model", pulp.LpMinimize)
    pusha = pulp.LpVariable('a', lowBound=0, upBound=None, cat=pulp.LpInteger)
    pushb = pulp.LpVariable('b', lowBound=0, upBound=None, cat=pulp.LpInteger)
    m += pusha * ax + pushb * bx == prize[0]
    m += pusha * ay + pushb * by == prize[1]
    m += pusha * 3 + pushb
    status = m.solve(pulp.PULP_CBC_CMD(msg=False, warmStart=True))
    if status == -1:
        continue
    else:
        print('HERE')
        tokens += 3 * pusha.value() + pushb.value()
    # print(status)
    # print(pusha.value(), pushb.value())
    # min   3x + y
    # s.t.  x * a[0] + y * b[0] = p[0]
    #       x * a[1] + y * a[1] = p[1]
    #       x, y >= 0, integer
    # A = npa([[ax, bx], [ay, by]])
    # print(A, prize)
    # cons = LinearConstraint(A, lb=prize, ub=prize)
    # opt = milp(c=[3, 1], integrality=[1,1], constraints=cons)

    # if opt.success:
    #     print(machines.index([a,b,p]), opt.mip_gap, opt.message)
    #     pusha, pushb = opt.x
    #     pusha = int(pusha)
    #     pushb = int(pushb)
    #     if pusha * ax + pushb * bx == prize[0] and pusha * ay + pushb * by == prize[1]:
    #         tokens2 += pusha * 3 + pushb
        # if resx * 
    
    print(tokens2)


# 69002373650697.0 too low
# 69002373650697.0
# 42081845479460
# 55145616865515
# 10980004135968
# 21767355942096
# 1013331388543
# 
print(tokens2)