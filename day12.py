from helpers import *

with open('day12_input.txt', 'r') as f:
    text = f.read()

text = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
text = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
text = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

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
    area = len(pts)
    
    all_border : Dict[Tuple, int] = {}
    for pt in pts:
        x,y = pt
        all_border[(x,y,0)] = 1
        all_border[(x+1,y,0)] = 1
        all_border[(x,y,1)] = 1
        all_border[(x,y+1,1)] = 1
    
    def not_internal(border):
        x, y, direction = border
        if direction:
            return (x,y) not in bounds or (x,y-1) not in bounds or A[x,y] != A[x,y-1]
        else:
            return (x,y) not in bounds or (x-1,y) not in bounds or A[x,y] != A[x-1,y]

    region_borders = {v : all_border[v] for v in all_border if not_internal(v)}

    change = True
    while change:
        print(len(region_borders))
        print({v : region_borders[v] for v in sorted(region_borders.keys())}, '\n')
        change = False
        for key in region_borders:
            x, y, direction = key
            old_len = region_borders[key]
            if direction: # vertical
                if (x+old_len, y, direction) in region_borders:
                    if (x,y) not in bounds or A[x,y] == A[x+old_len,y] or ((x+old_len, y-1) in bounds and A[x,y-1] == A[x+old_len,y-1]):
                        change = True
                        add_len = region_borders.pop((x+old_len, y, direction))
                        region_borders[key] += add_len
                        break
            else: # horizontal
                if (x, y+old_len, direction) in region_borders:
                    if (x,y) not in bounds or A[x,y] == A[x,y+old_len] or ((x-1, y+old_len) in bounds and A[x-1,y+old_len] == A[x-1,y+old_len]):
                        change = True
                        add_len = region_borders.pop((x, y+old_len, direction))
                        region_borders[key] += add_len
                        break

    perim = len(region_borders)
    return area * perim

res2 = get_price(price2)
print(f'Pt2: {res2}')