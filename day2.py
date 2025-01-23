from helpers import *

with open('day2_input.txt', 'r') as f:
    text = f.read().strip()

lines = [lmap(int, report.split()) for report in text.splitlines()]

# pt1
def good(line : List[int]) -> bool:
    ns = np.diff(line)
    return ((ns > 0).all() or (ns < 0).all()) and np.allclose(np.abs(ns), 2, atol=1)

print('Part 1:', sum(map(good, lines)))

# pt2
def good2(line):
    ''' Brute force deletion '''
    return good(line) or any(good(np.delete(line, i)) for i in range(len(line)))
        
print('Part 2:', sum(map(good2, lines)))