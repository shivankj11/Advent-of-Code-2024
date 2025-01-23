from helpers import *

with open('day22_input.txt', 'r') as f:
    text = f.read().strip()

nums = lmap(int, text.splitlines())

# pt1
def sim(n):
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    return n

def loop(n):
    for _ in range(2000):
        n = sim(n)
    return n

print(f'Part 1:', sum(map(loop, nums)))


# pt2
def get_seqs(nums) -> np.ndarray:
    A = np.empty((len(nums), 2001), dtype=int)
    for i in range(len(nums)):
        n = nums[i]
        A[i,0] = n % 10
        for j in range(1, 2001):
            n = sim(n)
            A[i,j] = n % 10
    changes = np.diff(A)
    seqs = {tuple(v) for L in changes for v in sw(L, 4)}
    return A, changes, seqs

A, changes, seqs = get_seqs(nums)
best_banana = 0
ct = 0
for seq in seqs:
    curr = 0
    for i in range(len(changes)):
        line = changes[i]
        sell_time = find_seq(line, seq) + 4
        if sell_time.size:
            curr += A[i][sell_time[0]]
    best_banana = max(best_banana, curr)
    ct += 1
    print(f'Progress: {ct} / {len(seqs)}', end='\r')

print(f'\nPart 2: {best_banana}')