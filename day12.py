from helpers import *

with open('day12_input.txt', 'r') as f:
    text = f.read()

text = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
# text2 = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

chars = set(text)
chars.remove('\n')
A = npa(lmap(list, text.split('\n')))
bounds = set(mesh(*A.shape))

def get_price(price_fn : Callable) -> int:
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
            price += price_fn(curr)
            seen = seen.union(curr)
    return price

# pt1
def price1(pts):
    area = len(pts)
    perim = 4 * area
    for pt in pts:
        neighbors = filter(lambda x : x in bounds, grid_neighbors(pt))
        perim -= sum(1 for v in neighbors if A[v] == A[pt])
    return area * perim

res1 = get_price(price1)
print(f'Pt1: {res1}')

# pt2
def price2(pts):
    print(pts)
    area = len(pts)
    borders = lmap()
    perim = 0

    return area * perim

res2 = get_price(price2)
print(f'Pt2: {res2}')