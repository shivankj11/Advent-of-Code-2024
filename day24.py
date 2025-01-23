from helpers import *

with open('day24_input.txt', 'r') as f:
    text = f.read().strip()

presets, operations = lmap(str.splitlines, text.split('\n\n'))
vals = {n : int(v) for n,v in [line.split(': ') for line in presets]}
instructions = []
for line in operations:
    lhs, out = line.split(' -> ')
    a, op_str, b = lhs.split()
    match op_str:
        case 'AND': operation = op.and_
        case 'OR': operation = op.or_
        case 'XOR': operation = op.xor
    instructions.append((operation, a, b, out))

# pt1
calc_var = lambda c,V : sum(V[v] << int(v[1:]) for v in V if v.startswith(c))

def get_vals(instructions, vals):
    I, V = deepcopy(instructions), deepcopy(vals)
    while I:
        op, a, b, out = I.pop(0)
        if a in V and b in V:
            V[out] = op(V[a], V[b])
        else:
            I.append((op, a, b, out))
    return V

print('Part 1:', calc_var('z', get_vals(instructions, vals)))

# pt2
def test_cases(vals) -> List[Dict]:
    tcs = []
    nvals = deepcopy(vals)
    tcs.append(nvals)
    nvals['x03'] = 1 - nvals['x03']
    nvals['x12'] = 1 - nvals['x12']
    nvals['y23'] = 1 - nvals['y23']
    nvals['y01'] = 1 - nvals['y01']
    nvals00 = deepcopy(vals)
    tcs.append(nvals00)
    nvals00['x00'] = 1
    nvals00['y00'] = 1
    nvals00['x01'] = 1
    nvals00['y01'] = 0
    nvals000 = deepcopy(vals)
    tcs.append(nvals000)
    nvals000['x00'] = 1
    nvals000['y00'] = 1
    nvals000['x01'] = 1
    nvals000['y01'] = 0
    nvals000['x02'] = 1 - nvals000['x02']
    nvals001 = deepcopy(vals)
    tcs.append(nvals001)
    nvals001['x00'] = 1
    nvals001['y00'] = 1
    nvals001['x01'] = 0
    nvals001['y01'] = 1
    nvals001['y02'] = 1 - nvals001['y02']
    nvals002 = deepcopy(vals)
    tcs.append(nvals002)
    nvals002['x00'] = 1
    nvals002['y00'] = 1
    nvals002['x01'] = 1
    nvals002['y01'] = 0
    nvals002['y02'] = 1 - nvals002['y02']
    nvals003 = deepcopy(vals)
    tcs.append(nvals003)
    nvals003['x00'] = 1
    nvals003['y00'] = 1
    nvals003['x01'] = 1
    nvals003['y01'] = 0
    nvals003['x02'] = 0
    nvals003['y02'] = 0
    nvals0 = deepcopy(vals)
    tcs.append(nvals0)
    nvals0['x04'] = 1
    nvals0['y04'] = 1
    nvals0['y05'] = 1
    nvals0['x05'] = 0
    nvals01 = deepcopy(vals)
    tcs.append(nvals01)
    nvals01['x04'] = 0
    nvals01['y04'] = 1
    nvals01['y05'] = 1
    nvals01['x05'] = 1
    nvals02 = deepcopy(vals)
    tcs.append(nvals02)
    nvals02['x04'] = 1
    nvals02['y04'] = 1
    nvals02['y05'] = 0
    nvals02['x05'] = 1
    nvals45 = deepcopy(vals)
    tcs.append(nvals45)
    nvals45['x03'] = 1
    nvals45['y03'] = 1
    nvals45['y04'] = 1
    nvals45['x04'] = 0
    nvals452 = deepcopy(vals)
    tcs.append(nvals452)
    nvals452['x03'] = 0
    nvals452['y03'] = 1
    nvals452['y04'] = 1
    nvals452['x04'] = 1
    nvals453 = deepcopy(vals)
    tcs.append(nvals453)
    nvals453['x03'] = 1
    nvals453['y03'] = 1
    nvals453['y04'] = 0
    nvals453['x04'] = 1
    nvals2 = deepcopy(vals)
    tcs.append(nvals2)
    nvals2['x13'] = 1 - nvals2['x13']
    nvals2['x21'] = 1 - nvals2['x21']
    nvals2['y33'] = 1 - nvals2['y33']
    nvals2['y07'] = 1 - nvals2['y07']
    nvals2['y17'] = 1 - nvals2['y17']
    nvals2['y27'] = 1 - nvals2['y27']
    nvals3 = deepcopy(vals)
    tcs.append(nvals3)
    nvals3['x01'] = 1 - nvals3['x01']
    nvals3['y02'] = 1 - nvals3['y02']
    nvals3['y12'] = 1 - nvals3['y12']
    nvals3['x08'] = 1 - nvals3['x08']
    nvals3['y32'] = 1 - nvals3['y32']
    nvals3['y33'] = 1 - nvals3['y33']
    nvals4 = deepcopy(vals)
    tcs.append(nvals4)
    nvals4['x00'] = 1
    nvals4['y00'] = 1
    nvals4['x01'] = 0
    nvals4['y01'] = 1
    nvals42 = deepcopy(vals)
    tcs.append(nvals42)
    nvals42['x20'] = 1
    nvals42['y20'] = 1
    nvals43 = deepcopy(vals)
    tcs.append(nvals43)
    nvals43['x20'] = 1
    nvals43['y20'] = 0
    nvals44 = deepcopy(vals)
    tcs.append(nvals44)
    nvals44['x20'] = 1
    nvals44['y20'] = 1
    nvals44['y21'] = 1
    nvals44['x21'] = 0
    nvals5 = deepcopy(vals)
    tcs.append(nvals5)
    nvals5['x16'] = 1 - nvals5['x16']
    nvals5['y39'] = 1 - nvals5['y39']
    nvals5['x40'] = 1 - nvals5['x40']
    nvals52 = deepcopy(vals)
    tcs.append(nvals52)
    nvals52['x38'] = 1
    nvals52['y38'] = 1
    nvals6 = deepcopy(vals)
    tcs.append(nvals6)
    nvals6['x06'] = 1 - nvals6['x06']
    nvals6['x20'] = 1 - nvals6['x20']
    nvals6['y16'] = 1 - nvals6['y16']
    nvals6['x39'] = 1 - nvals6['x39']
    nvals6['y39'] = 1 - nvals6['y39']
    nvals7 = deepcopy(vals)
    nvals7['x20'] = 1
    nvals7['y20'] = 0
    nvals7['y21'] = 1
    nvals7['x21'] = 0
    tcs.append(nvals7)
    nvals8 = deepcopy(vals)
    nvals8['x20'] = 1
    nvals8['y20'] = 1
    nvals8['y21'] = 0
    nvals8['x21'] = 1
    tcs.append(nvals8)
    return tcs


def sort_ops(instructions, vals) -> str:
    I, V = deepcopy(instructions), deepcopy(vals)
    for i in range(len(I)):
        opf, a, b, out = I[i]
        if a.startswith('y') and b.startswith('x'):
            I[i] = (opf, b, a, out)
    I = sorted(I, key=lambda v : v[1])
    ordered_ops = ''
    while I:
        opf, a, b, out = I.pop(0)
        if a in V and b in V:
            V[out] = opf(V[a], V[b])
            op_str = 'AND' if opf == op.and_ else ('OR' if opf == op.or_ else 'XOR')
            ordered_ops += '\n' + ' '.join([a, op_str, b, '->', out])
        else:
            I.append((opf, a, b, out))
    return ordered_ops.strip()


def create_G(instructions) -> DefaultDict:
    """
        Returns a dictionary mapping each output to
        the set of all inputs required to calculate it
    """
    outputs = {v[-1] for v in instructions}
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


def switch_out(instructions, o1, o2) -> bool:
    """
        Modifies instructions in place
        
        RETURNS
            True if switch can be made, False otherwise
    """
    G = create_G(instructions)
    if o1 in G[o2] or o2 in G[o1]:
        return False
    i_map = {instructions[i][-1] : i for i in range(len(instructions))}
    a,b,c,_ = instructions[i_map[o1]]
    d,e,f,_ = instructions[i_map[o2]]
    instructions[i_map[o1]], instructions[i_map[o2]] = (a,b,c,o2), (d,e,f,o1)
    return True


def w(instructions, s):
    s = sort_ops(instructions, vals).strip().splitlines()
    prev = 90
    i = 90
    pieces = []
    while i < len(s):
        line = s[i]
        out = line.split()[-1]
        if out.startswith('z'):
            pieces.append(s[prev:i+1])
            prev = i+1
        i += 1
    pieces.append(s[prev:])

    i = 0
    news = ''
    while i < 90:
        line = s[i]
        a = line.split()[0]
        if a.startswith('x'):
            news += '\n' + '\n'.join(pieces[int(a[1:])])
        news += ('\n' + line)
        i += 1
    with open('day24_input_sorted.txt', 'w') as f:
        f.write(s)


def print_z_instr(full=False) -> None:
    m = {}
    def make(v1, opf, v2, d=0) -> str:
        if v1.startswith('x') or d > 2:
            return f'{v1} {opf} {v2}'
        else:
            new_d = d if full else d+1
            lhs = make(*operations[m[v1]].split()[:3], d=new_d)
            rhs = make(*operations[m[v2]].split()[:3], d=new_d)
            return f'({lhs}) {opf} ({rhs})'
    operations = sort_ops(instructions, vals).strip().splitlines()
    for i in range(len(operations)):
        v = operations[i].split()
        out = v[-1]
        m[out] = i
    for i in range(46):
        z = 'z' + ('0' if i < 10 else '') + str(i)
        v1, opf, v2, _, _ = operations[m[z]].split()
        full = make(v1, opf, v2)
        print(z + " = " + full + '\n\n')


def wrong_z(V) -> Set[str]:
    x = calc_var('x', V)
    y = calc_var('y', V)
    z = bin(x+y)[::-1]
    zs = {v : V[v] for v in V if v.startswith('z')}
    wrong = set()
    for i in range(len(zs)):
        si = 'z' + ('0' if i < 10 else '') + str(i)
        if int(z[i]) != zs[si]:
            wrong.add(si)
    return wrong


def wrongs(instructions, *switches) -> Set[str]:
    """
        Tests set of switches with instructions on all test cases
    
        RETURNS
            Set of all z values that were incorrect in any test case
    """
    instructions = deepcopy(instructions)
    
    all_switches_possible = True
    for v1, v2 in switches:
        if v1 == v2:
            continue
        all_switches_possible = all_switches_possible and switch_out(instructions, v1, v2)
    
    if not all_switches_possible:
        raise Exception()
    
    Vs = [wrong_z(get_vals(instructions, vs)) for vs in test_cases(vals)]
    return reduce(set.union, Vs, set())


I = instructions
for v1,v2 in [('gmq','z21'), ('frn', 'z05'), ('wnf', 'vtj'), ('z39', 'wtt')]: # ('frn', 'srp'),
    switch_out(I, v1, v2)
answer = ('gmq', 'z21', 'frn', 'z05', 'wnf', 'vtj', 'z39', 'wtt')
print('Part 2:', ','.join(sorted(answer)))


# Below are attempts to do this programmatically
def garbage():
    def affecting_outputs(I, V) -> Set:
        G = create_G(I)
        wrongs = wrong_z(get_vals(instructions, V))
        return wrongs.union(reduce(set.union, (G[v] for v in wrongs), set()))
    if input('b compute?'):
        for switches, _ in b:
            print(switches)
            temp_instr = deepcopy(instructions)
            switch_out(temp_instr, switches[1], switches[0])
            V = get_vals(temp_instr, vals)
            V2 = get_vals(temp_instr, nvals)
            V3 = get_vals(temp_instr, nvals2)
            if wrong_z(V) == wrong_z(V2) == wrong_z(V3):
                print(switches, v)
            for v in vals:
                if v.startswith('z'):
                    continue
                temp_instr = deepcopy(instructions)
                switch_out(temp_instr, 'fqr', switches[0])
                switch_out(temp_instr, switches[0], switches[1])
                V = get_vals(temp_instr, vals)
                V2 = get_vals(temp_instr, nvals)
                V3 = get_vals(temp_instr, nvals2)
                if wrong_z(V) == wrong_z(V2) == wrong_z(V3):
                    print(switches, '1', v)
                temp_instr = deepcopy(instructions)
                switch_out(temp_instr, 'fqr', switches[1])
                switch_out(temp_instr, switches[0], switches[1])
                V = get_vals(temp_instr, vals)
                V2 = get_vals(temp_instr, nvals)
                V3 = get_vals(temp_instr, nvals2)
                if wrong_z(V) == wrong_z(V2) == wrong_z(V3):
                    print(switches, '2', v)

    dpairs = {v for v in pairs if not v[0].startswith('z') and not v[1].startswith('z')}
    worked = []
    for p1,p2 in dpairs:
        t = deepcopy(instructions)
        switch_out(t, p1, p2)
        V = get_vals(t, vals)
        V2 = get_vals(t, nvals)
        V3 = get_vals(t, nvals2)
        if wrong_z(V) == wrong_z(V3):
            print(p1,p2)
            worked.append((p1, p2))

    worked2 = []
    for p1,p2 in worked:
        t = deepcopy(instructions)
        switch_out(t, p1, p2)
        V = get_vals(t, vals)
        V2 = get_vals(t, nvals)
        V3 = get_vals(t, nvals2)
        if wrong_z(V2) == wrong_z(V3):
            print(p1,p2)
            worked2.append((p1, p2))
