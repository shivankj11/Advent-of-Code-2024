from helpers import *

with open('day3_input.txt', 'r') as f:
    text = f.read()

# pt1
def get_res(text):
    pattern = r"mul\((\d+,\d+)\)"
    res = re.findall(pattern, text)
    return sum(int(x) * int(y) for x,y in map(lambda s : s.split(','), res))

print(get_res(text))

# pt2
text2 = text
while text2.find("don't") != -1:
    idx = text2.find("don't()")
    enable = text2.find("do()", idx)
    if enable != -1:
        text2 = text2[:idx] + text2[enable:]
    else:
        text2 = text2[:idx]

print(get_res(text2))