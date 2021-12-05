with open("in.txt") as f:
    s = f.read()

v = [x for x in s.splitlines() if x != '']

b1 = [int(x) for x in v[0].split(',')]

b = v[1:]

def splitempty(s):
    return [[int(x), False] for x in s.split(' ') if x != '']

boards = [[splitempty(a), splitempty(b), splitempty(c), splitempty(d), splitempty(e)] for a,b,c,d,e in zip(b[::5], b[1::5], b[2::5], b[3::5], b[4::5])]

def iscompleterow(board, row):
    return all(x[1] for x in board[row])

def iscompletecol(board, col):
    return all(r[col][1] for r in board)


def iscomplete(board):
    return any([iscompleterow(board, row) for row in range(5)]) or \
         any([iscompletecol(board, col) for col in range(5)])

def updb(board, v):
    for row in range(5):
        for col in range(5):
            if board[row][col][0] == v:
                board[row][col][1] = True

def sc(board, v):
    s = 0
    for row in board:
        for x in row:
            if x[1] == False:
                s += x[0]
    return s * v

def compute():
    for bingov in b1:
        for bind in range(len(boards)):
            updb(boards[bind], bingov)
            
            if iscomplete(boards[bind]):
                return sc(boards[bind], bingov)
            
def compute2():
    remaining = list(range(len(boards)))

    for bingov in b1:
        for bind in range(len(boards)):
            if bind not in remaining:
                continue
            updb(boards[bind], bingov)
            
            if iscomplete(boards[bind]):
                remaining.remove(bind)
                if len(remaining) == 0:
                    return sc(boards[bind], bingov)
print(compute())
print(compute2())
