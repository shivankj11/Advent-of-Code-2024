from helpers import *

# Input
A, B, C = 65804993, 0, 0
program = [2, 4, 1, 1, 7, 5, 1, 4, 0, 3, 4, 5, 5, 5, 3, 0]


# pt1
def get_output(A, B, C, program) -> List[int]:
    output = []
    i = 0
    while i < len(program):
        instruction, operand = program[i], program[i+1]
        if instruction in {0, 2, 5, 6, 7}:
            match operand:
                case 4: operand = A
                case 5: operand = B
                case 6: operand = C
        match instruction:
            case 0: A = A // (2 ** operand)
            case 1: B = B ^ operand
            case 2: B = operand % 8
            case 3:
                if A != 0:
                    i = operand - 2
            case 4: B = B ^ C
            case 5:
                output.append(operand % 8)
            case 6: B = A // (2 ** operand)
            case 7: C = A // (2 ** operand)
        i += 2
    return output

print(",".join(map(str, get_output(A, B, C, program))))


# pt2
def print_output(A) -> List[int]:
    output = []
    B, C = 0, 0
    while A:
        print(f'A = {bin(A)[2:]}, B = {bin(B)[2:]}, C = {bin(C)[2:]}')
        # 1) B = last 3 bits of A
        B = A % 8
        # 2) Flip last bit of B
        B ^= 1
        print(f'A = {bin(A)[2:]}, B = {bin(B)[2:]}, C = {bin(C)[2:]}')
        # 3) C = last 3 bits of A >> B
        C = (A >> B) % 8
        print(f'A = {bin(A)[2:]}, B = {bin(B)[2:]}, C = {bin(C)[2:]}')
        # 4) flip first bit of B
        B ^= 4
        print(f'A = {bin(A)[2:]}, B = {bin(B)[2:]}, C = {bin(C)[2:]}')
        # 5) OUTPUT (B ^ C)
        output.append(((B ^ C)))
        print('OUTPUT', (B ^ C))
        # 6) Chop last 3 bits of A
        A >>= 3
    return output

def test_output_match(A) -> bool:
    i = 0
    j = 0
    while i < len(program):
        instruction, operand = program[i], program[i+1]
        if instruction in {0, 2, 5, 6, 7}:
            match operand:
                case 4: operand = A
                case 5: operand = B
                case 6: operand = C
        match instruction:
            case 0: A = A // (2 ** operand)
            case 1: B = B ^ operand
            case 2: B = operand % 8
            case 3:
                if A != 0:
                    i = operand - 2
            case 4: B = B ^ C
            case 5:
                if j >= len(program) or operand % 8 != program[j]:
                    return False
                j += 1
            case 6: B = A // (2 ** operand)
            case 7: C = A // (2 ** operand)
        i += 2
    return True

def loop_output_match(try_A=0) -> int:
    try_A = int(590e6)
    while not test_output_match(try_A):
        try_A += 1
        if try_A % 1e7 == 0:
            print(f'A = {int(try_A // 1e7)}0M')

# 882387498 gives [2, 4, 1, 1, 7, 5, 1, 4, 0, 3], need [4, 5, 5, 5, 3, 0]
# print(loop_output_match(try_A = int(590e6)))

def run(A) -> List[int]:
    output = []
    B, C = 0, 0
    while A:
        B = A % 8 ^ 1
        C = (A >> B) % 8
        B ^= 4
        output.append(B ^ C)
        A >>= 3
    return output

def rep2(A):
    A = lmap(int, bin(A)[2:])
    output = []
    while A:
        i = 0
        B = 0
        p = 0
        for v in A[-3-i:]:
            B += 2 ** p if v else 0
            p += 1
        print('B =', bin(B)[2:])
        B ^= 1
        C = 0
        p = 1
        for v in A[-3-i-B:-i-B]:
            C += 2 ** p if v else 0
            p += 1
        print('C =', bin(C)[2:])
        B ^= 4
        output.append(B ^ C)
        try:
            A.pop()
            A.pop()
            A.pop()
        except:
            return output
    return output

def mka(program, A=0, i=0):
    """ backtracking on 3-bit groups of A """
    if i == len(program):
        if run(A) == program:
            return A
        else:
            return -1
    v = program[i]
    for new in range(8):
        for new2 in range(8):
            if new ^ 1 ^ 4 ^ new2 == program[i]:
                A_try = mka(program, A=A+(new << (3 * i)), i=i+1)
                if A_try != -1:
                    return A_try
                break
    return -1
