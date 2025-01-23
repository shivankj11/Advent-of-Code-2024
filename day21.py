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
pair_map = {
        ('A', '<') : 'v<<', ('A', '^') : '<', ('A', 'v') : '<v',
        ('A', '>') : 'v', ('^', 'A') : '>', ('^', '<') : 'v<',
        ('^', '>') : 'v>', ('^', 'v') : 'v', ('<', 'v') : '>',
        ('<', '^') : '>^', ('<', '>') : '>>', ('<', 'A') : '>>^',
        ('v', '<') : '<', ('v', '>') : '>', ('v', '^') : '^',
        ('v', 'A') : '^>', ('>', '<') : '<<', ('>', 'v') : '<',
        ('>', 'A') : '^', ('>', '^') : '<^', ('^', 'v') : 'v',
        ('^', '>') : 'v>', ('^', 'A') : '>', ('v', 'v') : '',
        ('A', 'A') : '', ('^', '^') : '', ('<', '<') : '', ('>', '>') : '',    
}

def verify(moves, k):
    """ Returns output moves from applying moves to series of k robots """
    def move_to_button(moves : Iterable[str], keypad : np.ndarray[str]) -> str:
        """
            INPUTS:
                moves : Sequence of strings representing moves on the directional keypad
                keypad : 2D array representing the target keypad layout
            
            RETURNS:
                A string of the buttons pressed on given keypad by the given sequence of moves on the directional keypad
        """
        x, y = arr_find(keypad)('A')
        buttons = []
        for move in moves:
            match move:
                case '<': y -= 1
                case '>': y += 1
                case 'v': x += 1
                case '^': x -= 1
                case _: buttons.append(keypad[x, y])
        return buttons
    
    for _ in range(k):
        moves = move_to_button(moves, directional)

    return move_to_button(moves, numeric)

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
    print(f'Part 1: {complexity}')

# pt2
def shortest_moves_bf(moves, k) -> int:
    """ Computes shortest move string for a given code and number of robots """
    for _ in range(k):
        move_pairs = [('A', moves[0])]
        for i in range(len(moves)-1):
            t = (moves[i], moves[i+1])
            move_pairs.append(t)
        moves = "A".join(lmap(lambda x : pair_map[x], move_pairs)) + 'A'
    return len(moves)

def shortest_move_dp(moves, k) -> int:
    move_pairs = Counter(it.pairwise(moves))
    move_pairs['A', moves[0]] += 1
    for _ in range(k):
        new_pairs = defaultdict(int)
        for p in move_pairs:
            ct = move_pairs[p]
            adding = 'A' + pair_map[p] + 'A'
            for v in it.pairwise(adding):
                new_pairs[v] += ct
        move_pairs = new_pairs
    return sum(move_pairs.values())

def best_moves(code, k=25, best_move_f=shortest_move_dp):
    """
        Computes size of shortest move string for a given code and number of robots
        
        Stores pairs of moves in move string as count of pairs of moves
    """
    movesL = get_moves(numeric, code)
    best = np.inf
    for moves in movesL:
        shortest = best_move_f(moves, k)
        best = min(best, shortest)
    return best

complexity2 = sum(best_moves(code) * int(code[:-1]) for code in codes)
print(f'Part 2: {complexity2}')