from helpers import *

# Input
codes = ['539A', '964A', '803A', '149A', '789A']
numeric = npa([
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['X', '0', 'A']
])
directional = npa([
    ['X', '^', 'A'],
    ['<', 'v', '>']
])
def verify_k(moves, k=2) -> str:
    x, y = arr_find(directional)('A')
    for _ in range(k):
        moves_new = []
        for move in moves:
            match move:
                case '<': y -= 1
                case '>': y += 1
                case 'v': x += 1
                case '^': x -= 1
                case _: moves_new.append(directional[x, y])
        moves = moves_new
    x, y = arr_find(numeric)('A')
    code = ''
    for move in moves:
        match move:
            case '<': y -= 1
            case '>': y += 1
            case 'v': x += 1
            case '^': x -= 1
            case _: code += numeric[x, y]
    return code


# pt1
def get_moves(A, code) -> List[str]:
    """ Returns list of directional keypad moves to
        enter code in given keypad A """
    def get_move_opts(x, y, tx, ty, L) -> List[List[str]]:
        if (tx, ty) == (x, y):
            return L
        res = []
        if tx < x:
            if A[x-1, y] != 'X':
                res += get_move_opts(x-1, y, tx, ty, [v + '^' for v in L])
        elif tx > x:
            if A[x+1, y] != 'X':
                res += get_move_opts(x+1, y, tx, ty, [v + 'v' for v in L])
        if ty < y:
            if A[x, y-1] != 'X':
                res += get_move_opts(x, y-1, tx, ty, [v + '<' for v in L])
        elif ty > y:
            res += get_move_opts(x, y+1, tx, ty, [v + '>' for v in L])
        return res
    find = arr_find(A)
    x, y = find('A')
    move_options = ['']
    for button in code:
        tx, ty = find(button)
        move_options = get_move_opts(x, y, tx, ty, move_options)
        move_options = [L + 'A' for L in move_options]
        x, y = tx, ty
    return move_options


if input('Type "y" to compute Part 1: ') == 'y':
    complexity = 0
    for code in codes:
        r1 = get_moves(numeric, code)
        r2 = {m for ss in [get_moves(directional, v) for v in r1] for m in ss}
        r2_min = min(map(len, r2))
        moves = [map(len, get_moves(directional, v)) for v in r2 if len(v) == r2_min]
        complexity += min(map(min, moves)) * int(code[:-1])
    print(f'Part 1: Complexity = {complexity}')


# pt2
codes = ['029A', '980A', '179A', '456A', '379A'] # example
# 231564 pt 1 answer
def getbest(mpairs : Dict[str, int], first : str) -> Dict[str, int]:
    print(f'BEFORE:', mpairs)
    pair = {('A', '<') : 'v<<', ('A', '^') : '<', ('A', 'v') : 'v<',
            ('A', '>') : 'v', ('^', 'A') : '>', ('^', '<') : 'v<',
            ('^', '>') : 'v>', ('^', 'v') : 'v', ('<', 'v') : '>',
            ('<', '^') : '>^', ('<', '>') : '>>', ('<', 'A') : '>>^',
            ('v', '<') : '<', ('v', '>') : '>', ('v', '^') : '^',
            ('v', 'A') : '^>', ('>', '<') : '<<', ('>', 'v') : '<',
            ('>', 'A') : '^', ('>', '^') : '<^', ('^', 'v') : 'v',
            ('^', '<') : 'v<', ('^', '>') : 'v>', ('^', 'A') : '>'}
    # TODO A<->v, > <-> ^  /// don't need to?
    mpairs[('A', first)] = mpairs.get(('A', first), 0) + 1
    first = pair[('A', first)][0]
    result = defaultdict(int)
    for p in mpairs:
        if p in pair:
            adding = pair[p]
            if len(adding) == 1:
                t = ('A', adding)
                result[t] += mpairs[p]
                t = (adding, 'A')
                result[t] += mpairs[p]
            elif len(adding) == 2:
                t = ('A', adding[0])
                result[t] += mpairs[p]
                result[adding] += mpairs[p]
                t = (adding[1], 'A')
                result[t] += mpairs[p]
            else:
                t = ('A', adding[0])
                result[t] += mpairs[p]
                result[adding[:2]] += mpairs[p]
                result[adding[1:3]] += mpairs[p]
                t = (adding[-1], 'A')
                result[t] += mpairs[p]
        # result['A'] = result.get('A', 0) + mpairs[p]
    print('AFTER:', result)
    return result, first

k = 2
res = []
for code in codes[:1]:
    movesL = get_moves(numeric, code)
    best = 10e12
    for moves in movesL:
        print('MOVES:', moves)
        move_pairs = defaultdict(int)
        first = moves[0]
        for i in range(len(moves)-1):
            t = (moves[i], moves[i+1])
            move_pairs[t] += 1
        for _ in range(k):
            move_pairs, first = getbest(move_pairs, moves[0])
        best = min(best, 1 + sum(move_pairs.values()))
        break
    res.append(best)

complexity = 0
for c, code in zip(res, codes):
    complexity += c * int(code[:-1])