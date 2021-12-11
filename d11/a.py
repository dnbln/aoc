with open("in.txt") as f:
    s = f.read()
    
def parse(s):
    return [list(map(lambda x: int(x), list(l))) for l in s.splitlines() if l != '']

v = parse(s)

SIZE_X = len(v)
SIZE_Y = len(v[0])

def adj(x, y):
    v = []
    if x > 0:
        if y > 0:
            v.append((x - 1, y - 1))
        v.append((x - 1, y))
        if y < SIZE_Y-1:
            v.append((x - 1, y + 1))
    if y > 0:
        v.append((x, y - 1))
    if y < SIZE_Y - 1:
        v.append((x, y + 1))
    if x < SIZE_X - 1:
        if y > 0:
            v.append((x + 1, y - 1))
        v.append((x + 1, y))
        if y < SIZE_Y - 1:
            v.append((x + 1, y + 1))
    
    return v

def step(v):
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            v[i][j] += 1
        
    q = []
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            if v[i][j] > 9:
                v[i][j] = 0
                q.append((i, j))
                
    flashes = 0
    
    while len(q) != 0:
        x, y = q[0]
        q = q[1:]
        
        flashes += 1
        for a, b in adj(x, y):
            if v[a][b] != 0:
                v[a][b] += 1
                if v[a][b] > 9:
                    v[a][b] = 0
                    q.append((a, b))
                    
    return flashes

clv = v.copy()

fl = 0
for _ in range(100):
    fl += step(clv)
    
print(fl)

stp = 0
while True:
    stp += 1
    if step(v) == SIZE_X * SIZE_Y:
        break
print(stp + 2)
