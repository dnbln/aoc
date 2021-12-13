with open("in.txt") as f:
    s = f.read()
    

def parse(s):
    lines = s.splitlines()
    
    em = lines.index('')
    
    lx = lambda x: [x[0], int(x[1])]
    
    lc = lambda x: (int(x[0]), int(x[1]))
    
    return set([lc(l.split(',')) for l in lines[:em]]), \
         [lx(l.split(' ')[2].split('=')) for l in lines[em+1:] if l != '']

grid, folds = parse(s)

def applyFold(grid, fold):
    if fold[0] == 'x':
        x = fold[1]
        newgrid = set([])
        for point in grid:
            if point[0] > x:
                nx = x - (point[0] - x)
                ny = point[1]
                
                newgrid |= set([(nx, ny)])
            else:
                nx = point[0]
                ny = point[1]
                
                newgrid |= set([(nx, ny)])
    else:
        y = fold[1]
        newgrid = set([])
        for point in grid:
            if point[1] > y:
                nx = point[0]
                ny = y - (point[1] - y)
                
                newgrid |= set([(nx, ny)])
            else:
                nx = point[0]
                ny = point[1]
                
                newgrid |= set([(nx, ny)])
    return newgrid

ngrid = applyFold(grid, folds[0])
print(len(ngrid))

for fold in folds:
    grid = applyFold(grid, fold)
    
def pg(gr):
    g = [[' '] * 50 for _ in range(10)]
    for p in gr:
        g[p[1]][p[0]] = '#'
        
    for l in g:
        print(''.join(l))

pg(grid)