from helpers import *

with open('day23_input.txt', 'r') as f:
    text = f.read().strip()

text ='''
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''.strip()
pairs = lmap(lambda s : sorted(s.split('-')), text.splitlines())
connections = defaultdict(list)
for a,b in pairs:
    connections[a].append(b)
    connections[b].append(a)

# pt1
triples = set()
for a in connections:
    bs = connections[a]
    for b, c in it.combinations(bs, 2):
        if b in connections[c]:
            triples.add(tuple(sorted((a,b,c))))

ct = 0
for a,b,c in triples:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        ct += 1

print(f'Part 1:', ct)

# pt2
groups = []
for a in connections:
    bs = connections[a]

def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)
    
def dfs_util(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_util(graph, neighbor, visited)

def find_largest_scc(graph):
    visited = defaultdict(bool)
    stack = []

    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, stack)

    graph_rev = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            graph_rev[neighbor].append(node)

    visited = defaultdict(bool)
    scc = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc_component = []
            dfs_util(graph_rev, node, visited)
            scc.append(scc_component)

    largest_scc = max(scc, key=len)
    return len(largest_scc)
    

largest_scc_size = find_largest_scc(connections)
print(f"Part 2: {largest_scc_size}")