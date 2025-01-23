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
            case 0: A //= (2 ** operand)
            case 1: B ^= operand
            case 2: B = operand % 8
            case 3: i = operand - 2 if A else i
            case 4: B ^= C
            case 5: output.append(operand % 8)
            case 6: B = A // (2 ** operand)
            case 7: C = A // (2 ** operand)
        i += 2
    return output

print('Part 1:', ",".join(map(str, get_output(A, B, C, program))))

# pt2
def mka(program) -> int:
    """ Greedy algorithm on 3-bit groups of A
        + Ability to backtrack since A can increase by
        more than 0b111 for one program output
    """
    A = 0
    for i in range(len(program)):
        A <<= 3
        while get_output(A, 0, 0, program) != program[-i-1:]:
            A += 1
    return A

print('Part 2:', mka(program))


# Previous tries
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

class Testing():
    p1 = [0,3,5,4,3,0]

    def run1(A):
        output = []
        while A:
            A //= 8
            output.append(A % 8)
        return output

    def test1(program, A=0, i=0):
        if i == len(program):
            return A if Testing.run1(A) == program else -1
        for n in range(8):
            if n % 8 == program[i]:
                A_try = Testing.test1(program, A=A+(n << (3 * (i+1))), i=i+1)
                if A_try != -1:
                    return A_try
        return -1
    
    p2 = [2, 4, 1, 1, 0, 3, 5, 5, 3, 0]

    def run2(A):
        # program = [2, 4, 1, 1, 0, 3, 5, 5, 3, 0]
        output = []
        while A:
            output.append((A % 8) ^ 1)
            A >>= 3
        return output

    def test2(program, A=0, i=0):
        """ backtracking on 3-bit groups of A """
        if i == len(program):
            if Testing.run2(A) == program:
                return A
            else:
                return -1
        for n in range(8):
            if n ^ 1 == program[i]:
                A_try = Testing.test2(program, A=A+(n << (3 * i)), i=i+1)
                if A_try != -1:
                    return A_try
        return -1

    def test() -> None:
        print(f'Test 1 Program = {Testing.p1}, Result =', end=' ')
        res1 = Testing.test1(Testing.p1)
        print(f'{res1},\nResult Program = {Testing.run1(res1)}')
        print(f'Test 2 Program = {Testing.p2}, Result =', end=' ')
        res2 = Testing.test2(Testing.p2)
        print(f'{res2},\nResult Program = {Testing.run2(res2)}')

def run_fast(A) -> List[int]:
    output = []
    while A:
        B = A % 8 ^ 1
        C = (A >> B) % 8
        output.append(B ^ C ^ 4)
        A >>= 3
    return output
