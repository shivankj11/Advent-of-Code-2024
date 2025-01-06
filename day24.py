from helpers import *

with open('day24_input.txt', 'r') as f:
    text = f.read().strip()

presets, operations = lmap(str.splitlines, text.split('\n\n'))
vals = {n : int(v) for n,v in [line.split(': ') for line in presets]}
instructions = []
for line in operations:
    lhs, out = line.split(' -> ')
    a, op_str, b = lhs.split(' ')
    match op_str:
        case 'AND': operation = op.and_
        case 'OR': operation = op.or_
        case 'XOR': operation = op.xor
    instructions.append((operation, a, b, out))


# pt1
def apply_instructions(instructions, vals):
    I, V = deepcopy(instructions), deepcopy(vals)
    while I:
        op, a, b, out = I.pop(0)
        if a in V and b in V:
            V[out] = op(V[a], V[b])
        else:
            I.append((op, a, b, out))
    return sum(V[v] << int(v[1:]) for v in V if v.startswith('z'))

print('Part 1:', apply_instructions(instructions, vals))


# pt2


# get all depdencies of outputs
outputs = {v[-1] for v in instructions}

def create_G(instructions) -> DefaultDict:
    G = defaultdict(set)
    seen = set()
    for _, a, b, out in instructions:
        if a in vals and b in vals:
            seen.add(out)
    while len(seen) < len(outputs):
        for _,a,b,out in instructions:
            if a in seen and b in seen and out not in seen:
                seen.add(out)
                q = [a, b]
                searched = {a, b}
                while q:
                    v = q.pop()
                    searched.add(v)
                    G[out].add(v)
                    for n in G[v]:
                        if n not in searched:
                            q.append(n)
    return G

def get_vals(instructions, vals):
    I, V = deepcopy(instructions), deepcopy(vals)
    while I:
        op, a, b, out = I.pop(0)
        if a in V and b in V:
            V[out] = op(V[a], V[b])
        else:
            I.append((op, a, b, out))
    return V

V = get_vals(instructions, vals)

xs = {v : vals[v] for v in vals if v.startswith('x')}
ys = {v : vals[v] for v in vals if v.startswith('y')}

def wrong_z(V) -> Set[str]:
    x = sum(vals[v] << int(v[1:]) for v in vals if v.startswith('x'))
    y = sum(vals[v] << int(v[1:]) for v in vals if v.startswith('y'))
    z = x + y
    zs = {v : V[v] for v in V if v.startswith('z')}
    b = bin(z)[::-1]
    wrong = set()
    for i in range(len(zs)):
        if i < 10:
            si = 'z0' + str(i)
        else:
            si = 'z' + str(i)
        if int(b[i]) != zs[si]:
            wrong.add(si)
    return wrong

G = create_G(instructions)
affecting_outputs = lambda G, wrong : wrong.union(reduce(set.union, (G[v] for v in wrong)))

ao = affecting_outputs(G, wrong_z(V)) 
real_instr = npa(list(filter(lambda v : v[-1] in ao, instructions)))
print(ao.intersection(real_instr[:,-1]))

def switch_out(instructions, o1, o2) -> None:
    """ Modifies instructions in place """
    i_map = {instructions[i][-1] : i for i in range(len(instructions))}
    a,b,c,_ = instructions[i_map[o1]]
    instructions[i_map[o1]] = a,b,c,o2
    a,b,c,_ = instructions[i_map[o2]]
    instructions[i_map[o2]] = a,b,c,o1

def test(switches):
    global instructions
    instructions = deepcopy(instructions)
    for o1, o2 in switches:
        switch_out(instructions, o1, o2)
    newV = get_vals(instructions, vals)
    wrong_z(newV)
    print(len(wrong_z))

'''
    switching vhs & z21
'''
# for switch in it.combinations(affecting_outputs, 8):
#     I2 = deepcopy(instructions)
#     pos = [i_map[v] for v in switch]
#     o, a, b, _ = I2[i_map[v]]
