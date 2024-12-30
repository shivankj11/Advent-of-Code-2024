from helpers import *

with open('day22_input.txt', 'r') as f:
    text = f.read().strip()

nums = lmap(int, text.splitlines())

# pt1
def sim(n):
    for _ in range(2000):
        n ^= n * 64
        n %= 16777216
        n ^= n // 32
        n %= 16777216
        n ^= n * 2048
        n %= 16777216
    return n

print(f'Part 1:', sum(map(sim, nums)))


# pt2
nums = [1, 2, 3, 2024]
def get_seqs(nums) -> np.ndarray:
    A = np.empty((len(nums), 2001), dtype=int)
    for i in range(len(nums)):
        n = nums[i]
        A[i,0] = n % 10
        for j in range(1, 2001):
            n ^= n * 64
            n %= 16777216
            n ^= n // 32
            n %= 16777216
            n ^= n * 2048
            n %= 16777216
            A[i,j] = n % 10
    changes = np.diff(A)
    seqs = set()
    [seqs.add(tuple(v)) for L in changes for v in sw(L, 4)]
    return changes, seqs

seqs = 