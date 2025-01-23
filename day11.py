from helpers import *

stones = [814, 1183689, 0, 1, 766231, 4091, 93836, 46]

def rule(n : int) -> Union[int, Tuple[int, int]]:
    if n == 0:
        return 1
    s = str(n)
    if len(s) % 2:
        return n * 2024
    else:
        return int(s[:len(s)//2]), int(s[len(s)//2:])
 
def get_k(stones, k):
    cts = {v : 1 for v in stones}
    for _ in range(k):
        new_cts = defaultdict(int)
        for stone in cts:
            new = rule(stone)
            if type(new) == int:
                new_cts[new] += cts[stone]
            else:
                new_cts[new[0]] += cts[stone]
                new_cts[new[1]] += cts[stone]
        cts = new_cts
    return sum(cts.values())

# pt1
print('Part 1:', get_k(stones, 25))

# pt2
print('Part 2:', get_k(stones, 75))