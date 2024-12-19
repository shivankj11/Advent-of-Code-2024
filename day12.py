from helpers import *

with open('day12_input.txt', 'r') as f:
    text = f.read()

def get_price(text, price_fn : Callable) -> int:
    """ Returns price of given input """
    chars = set(text)
    chars.remove('\n')
    A = npa(lmap(list, text.split('\n')))
    bounds = arr_bounds(A)
    price = 0
    for c in chars:
        occurences = lmap(tuple, npa(np.where(A == c)).T)
        seen = set()
        for pt in occurences:
            if pt in seen:
                continue
            curr = {pt}
            added = True
            while added:
                added = False
                new = set()
                for pt in curr:
                    f = lambda x : x in bounds and A[x] == c and x not in curr
                    neighbors = filter(f, grid_neighbors(pt))
                    for n in neighbors:
                        added = True
                        new.add(n)
                curr = curr.union(new)
            price += price_fn(curr, A)
            seen = seen.union(curr)
    return price

# pt1
def price1(pts, A):
    area = len(pts)
    perim = 4 * area
    bounds = arr_bounds(A)
    for pt in pts:
        perim -= sum(1 for v in grid_neighbors(pt) if v in bounds and A[v] == A[pt])
    return area * perim

def test1():
    ex1 = """AAAA\nBBCD\nBBCC\nEEEC"""
    ex2 = """OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"""
    ex3 = """RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"""

    print('Testing Part 1...', end='')
    with suppress_stdout():
        result = get_price(ex1, price1)
    assert(result == 140)
    with suppress_stdout():
        result = get_price(ex2, price1)
    assert(result == 772)
    with suppress_stdout():
        result = get_price(ex3, price1)
    assert(result == 1930)
    print('Part 1 Correct')

test1()
print(f'Part 1 Answer: {get_price(text, price1)}')

# pt2

def price2(pts, A):
    area = len(pts)
    bounds = arr_bounds(A)
    def not_internal(border) -> bool:
        x, y, direction = border
        if direction:
            return (x,y) not in bounds or (x,y-1) not in bounds or A[x,y] != A[x,y-1]
        else:
            return (x,y) not in bounds or (x-1,y) not in bounds or A[x,y] != A[x-1,y]
    all_border : Dict[Tuple, int] = {}
    for pt in pts:
        x,y = pt
        all_border[(x,y,0)] = 1
        all_border[(x+1,y,0)] = 1
        all_border[(x,y,1)] = 1
        all_border[(x,y+1,1)] = 1
    region_borders = {v : all_border[v] for v in all_border if not_internal(v)}
    change = True
    while change:
        change = False
        for key in region_borders:
            x, y, direction = key
            old_len = region_borders[key]
            if direction: # vertical
                if (x+old_len, y, direction) in region_borders:
                    if ((x,y) not in bounds or
                        A[x,y] == A[x+old_len,y] or
                        ((x+old_len, y-1) in bounds and (x,y-1) in bounds and A[x,y-1] == A[x+old_len,y-1])):
                        change = True
                        add_len = region_borders.pop((x+old_len, y, direction))
                        region_borders[key] += add_len
                        break
            else: # horizontal
                if (x, y+old_len, direction) in region_borders:
                    if ((x,y) not in bounds or
                        A[x,y] == A[x,y+old_len] or
                        ((x-1, y+old_len) in bounds and (x-1,y) in bounds and A[x-1,y] == A[x-1,y+old_len])):
                        change = True
                        add_len = region_borders.pop((x, y+old_len, direction))
                        region_borders[key] += add_len
                        break
    return area * len(region_borders)

def test2():
    ex1 = """AAAA\nBBCD\nBBCC\nEEEC"""
    ex2 = """OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"""
    ex3 = """RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"""
    ex4 = """EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE"""
    ex5 = """AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA"""

    print('Testing Part 2...', end='')
    with suppress_stdout():
        result = get_price(ex1, price2)
    assert(result == 80)
    with suppress_stdout():
        result = get_price(ex2, price2)
    assert(result == 436)
    with suppress_stdout():
        result = get_price(ex3, price2)
    assert(result == 1206)
    with suppress_stdout():
        result = get_price(ex4, price2)
    assert(result == 236)
    with suppress_stdout():
        result = get_price(ex5, price2)
    assert(result == 368)
    print('Part 2 Correct')

test2()
print(f'Part 2 Answer: {get_price(text, price2)}')