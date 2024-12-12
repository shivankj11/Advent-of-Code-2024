from helpers import *
import gc

stones = [814, 1183689, 0, 1, 766231, 4091, 93836, 46]

def rule(n) -> Union[int, Tuple[int, int]]:
    if n == 0:
        return 1
    if len(str(n)) % 2:
        return n * 2024
    else:
        return int(str(n)[:len((str(n)))//2]), int(str(n)[len(str(n))//2:])
 
# pt1
def get_k(stones, k=25):
    for _ in range(k):
        news = []
        for stone in stones:
            new = rule(stone)
            if type(new) == int:
                news.append(new)
            else:
                news.append(new[0])
                news.append(new[1])
        stones = news
    return stones

res1 = get_k(stones)
print(len(res1))

# pt2
def map_k(n):
    if n in stone_map_25:
        L = stone_map_25[n]
    else:
        L = [n]
        for i in range(25):
            new = []
            for stone in L:
                n = rule(stone)
                if type(n) == int:
                    new.append(n)
                else:
                    new.append(n[0])
                    new.append(n[1])
            L = new
    print('Done 25')
    L_done = []
    L2 = []
    for n in L:
        if n in stone_map_25:
            L_done.extend(stone_map_25[n])
        else:
            L2.append(n)
    gc.collect()
    for _ in range(25):
        new = []
        for stone in L2:
            n = rule(stone)
            if type(n) == int:
                new.append(n)
            else:
                new.append(n[0])
                new.append(n[1])
        L2 = new
    print('Done 50')
    L = []
    tot = 0
    for n in L2:
        if n in stone_map_25:
            tot += len(stone_map_25[n])
        else:
            L.append(n)
    for n in L_done:
        if n in stone_map_25:
            tot += len(stone_map_25[n])
        else:
            L.append(n)
    gc.collect()
    for _ in range(25):
        new = []
        for stone in L:
            n = rule(stone)
            if type(n) == int:
                new.append(n)
            else:
                new.append(n[0])
                new.append(n[1])
        L = new
    print('Done', n)
    return len(L) + tot
    
stone_map_25 = {}
for i in range(100):
    stone_map_25[i] = get_k([i], k=25)
    print('here')

# tot = []
# for stone in stones:
#     tot.append(map_k(stone))
#     print(tot)

