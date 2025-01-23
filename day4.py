from helpers import *

with open('day4_input.txt', 'r') as f:
    text = f.read()

A = npa(lmap(list, text.split('\n')))
rows, cols = A.shape
bounds = arr_bounds(A)


# pt1
def search(idx : Tuple[int, int]) -> int:
    '''
        Returns number of times 'MAS' was found in
        A starting at position idx, assumes A[idx] = 'X'
    '''
    def match(pts) -> int:
        if any(tuple(pt) not in bounds for pt in pts.T):
            return 0
        return ''.join(A[*pts]) == 'MAS'
    
    pts = npa([idx] * 3, dtype=int).T
    offset = npa([1, 2, 3], dtype=int)
    zero = np.zeros(3, dtype=int)

    # horizontal
    finds = match(pts + [zero, offset])
    finds += match(pts - [zero, offset])
    # vertical
    finds += match(pts + [offset, zero])
    finds += match(pts - [offset, zero])
    # top left to bot right diagonal
    finds += match(pts + [offset, offset])
    finds += match(pts - [offset, offset])
    # other diagonal
    finds += match(pts + [-offset, offset])
    finds += match(pts + [offset, -offset])

    return finds

print('Part 1:', sum(map(search, find(A, 'X'))))

# pt2
def search2(idx) -> int:
    i, j = idx
    if not (1 <= i < rows-1 and 1 <= j < cols-1):
        return 0
    diag1 = (A[i-1, j-1], A[i+1, j+1])
    diag2 = (A[i-1, j+1], A[i+1, j-1])
    return 'M' in diag1 and 'M' in diag2 and 'S' in diag1 and 'S' in diag2

print('Part 2:', sum(map(search2, find(A, 'A'))))