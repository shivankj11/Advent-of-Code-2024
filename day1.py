from helpers import *

with open('day1_input.txt', 'r') as f:
    text = f.read()

L = npa(lmap(lambda v : lmap(int, v.split('   ')), text.splitlines()))

# pt 1
L.sort(axis=0)
print('Part 1:', np.sum(np.abs(np.diff(L, 1))))

# pt 2
cts = Counter(L[:,1])
print('Part 2:', sum(cts[n] * n for n in L[:,0]))