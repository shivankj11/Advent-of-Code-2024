from helpers import *

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
    cts = {v : 1 for v in stones}
    for _ in range(k):
        new_cts = {}
        for stone in cts:
            new = rule(stone)
            if type(new) == int:
                new_cts[new] = new_cts.get(new, 0) + cts[stone]
            else:
                new_cts[new[0]] = new_cts.get(new[0], 0) + cts[stone]
                new_cts[new[1]] = new_cts.get(new[1], 0) + cts[stone]
        cts = new_cts
    return sum(cts.values())

print(get_k(stones))

# pt2
print(get_k(stones, k=75))