from helpers import *

with open('day23_input.txt', 'r') as f:
    text = f.read().strip()

connections = defaultdict(set)
for a,b in (s.split('-') for s in text.splitlines()):
    connections[a].add(b)
    connections[b].add(a)

# pt1
triples = set()
for a in connections:
    bs = connections[a]
    for b,c in it.combinations(bs, 2):
        if b in connections[c]:
            triples.add(tuple(sorted((a,b,c))))

ct = sum(v.startswith('t') for group in triples for v in group)
print('Part 1:', ct)

# pt2
group = max_clique(connections)
print('Part 2:', ",".join(sorted(group)))