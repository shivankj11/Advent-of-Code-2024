from helpers import *

with open('day2_input.txt', 'r') as f:
    text = f.read()

reports : List[str] = text.strip().split('\n')
lines : List[List[int]] = [lmap(int, report.split(' ')) for report in reports]

# pt1
def good(line : List[int]) -> bool:
    ns = np.diff(line)
    return (all(ns > 0) or all(ns < 0)) and all(np.abs(ns) <= 3) and all(np.abs(ns) >= 1)

print(sum(map(good, lines)))

# pt2
def good2(line):
    if good(line):
        return True
    
    for i in range(len(line)):
        ns_del = [line[j] for j in range(len(line)) if j != i]
        if good(ns_del):
            return True

    return False
        
print(sum(map(good2, lines)))