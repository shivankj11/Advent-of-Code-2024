from helpers import *

with open('day4_input.txt', 'r') as f:
    text = f.read()

A = npa(lmap(list, text.split('\n')))
rows, cols = len(A), len(A[0])

# pt1
def match(m, a, s) -> bool:
    return A[m] == 'M' and A[a] == 'A' and A[s] == 'S'

def search(idx : Tuple[int, int]) -> int:
    i,j = idx
    finds = 0
    # horizontal
    if j + 3 < cols:
        finds += match((i,j+1), (i,j+2), (i,j+3))
    if j - 3 >= 0:
        finds += match((i,j-1), (i,j-2), (i,j-3))
    # vertical
    if i + 3 < rows:
        finds += match((i+1,j), (i+2,j), (i+3,j))
    if i - 3 >= 0:
        finds += match((i-1,j), (i-2,j), (i-3,j))
    # top left to bot right diagonal
    if i + 3 < rows and j + 3 < cols:
        finds += match((i+1,j+1), (i+2,j+2), (i+3,j+3))
    if i - 3 >= 0 and j - 3 >= 0:
        finds += match((i-1,j-1), (i-2,j-2), (i-3,j-3))
    # other diagonal
    if i + 3 < rows and j - 3 >= 0:
        finds += match((i+1,j-1), (i+2,j-2), (i+3,j-3))
    if i - 3 >= 0 and j + 3 < cols:
        finds += match((i-1,j+1), (i-2,j+2), (i-3,j+3))

    return finds

ct = sum(map(search, filter(lambda idx : A[idx] == 'X', mesh(rows, cols))))
print(ct)

# pt2
def search2(idx):
    i, j = idx
    diag1 = (A[i-1, j-1] == 'M' and A[i+1, j+1] == 'S') or (A[i-1, j-1] == 'S' and A[i+1, j+1] == 'M')
    diag2 = (A[i-1, j+1] == 'M' and A[i+1, j-1] == 'S') or (A[i-1, j+1] == 'S' and A[i+1, j-1] == 'M')
    return (diag1 and diag2)

ct2 = sum(map(search2, filter(lambda idx : A[idx] == 'A', it.product(range(1, rows-1), range(1, cols-1)))))
print(ct2)