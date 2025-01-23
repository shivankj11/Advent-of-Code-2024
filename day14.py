from helpers import *

with open('day14_input.txt', 'r') as f:
    text = f.read()

robots = text.strip().splitlines()
for i in range(len(robots)):
    pos, vel = robots[i].split(' ')
    pos = lmap(int, pos[2:].split(','))
    vel = lmap(int, vel[2:].split(','))
    robots[i] = (pos, vel)

# pt1
A = np.zeros((103, 101), int)
for pos, vel in robots:
    x = (pos[1] + 100 * vel[1]) % A.shape[0]
    y = (pos[0] + 100 * vel[0]) % A.shape[1]
    A[x,y] += 1

res1 = A[:51,:50].sum() * A[:51,51:].sum() * A[52:,:50].sum() * A[52:,51:].sum()
print('Part 1:', res1)

# pt2
def print_board(steps : int) -> None:
    A = np.full((103, 101), ' ')
    for pos, vel in robots:
        x = (pos[0] + steps * vel[0]) % A.shape[1]
        y = (pos[1] + steps * vel[1]) % A.shape[0]
        A[y,x] = 'X'
    for line in A:
        print(line.tolist())

print('Part 2: 6771')
print_board(6771)

start = input('Print boards starting from which number? (enter to skip)')
if start:
    ct = int(start)
    while True:
        ct += 1
        print(ct)
        print_board(ct)
        time.sleep(.15)