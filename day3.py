from helpers import *

with open('day3_input.txt', 'r') as f:
    text = f.read()

# pt1
def get_res(text):
    pattern = r"mul\((\d+,\d+)\)"
    res = re.findall(pattern, text)
    return sum(int(x) * int(y) for x,y in map(lambda s : s.split(','), res))

print('Part 1:', get_res(text))

# pt2
while text.find("don't") != -1:
    idx = text.find("don't()")
    enable = text.find("do()", idx)
    if enable != -1:
        text = text[:idx] + text[enable:]
    else:
        text = text[:idx]

print('Part 2:', get_res(text))