with open('day1_input.txt', 'r') as f:
    s = f.read()

L = [v.split('   ') for v in s.strip().split('\n')]
L1 = [int(x[0]) for x in L]
L2 = [int(x[1]) for x in L]
d = {}
for n in L2:
    d[n] = d.get(n, 0) + 1
tot = 0
for n in L1:
    tot += d[n] * n if n in d else 0
print(tot)