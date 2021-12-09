with open("in.txt") as f:
    s = f.read()

def parse(s):
    return [[int(a) for a in list(x)] for x in s.splitlines() if x != '']

hm = parse(s)

# part 1
r = 0
n = len(hm)
m = len(hm[0])
def low(hm, i, j):
    return hm[i][j] < (hm[i][j+1] if j+1 < m else 10) and \
           hm[i][j] < (hm[i][j-1] if j-1 >=0 else 10) and \
           hm[i][j] < (hm[i-1][j] if i-1 >=0 else 10) and \
           hm[i][j] < (hm[i+1][j] if i+1 < n else 10)

for i in range(n):
    for j in range(m):
        if low(hm, i, j):
            r += hm[i][j] + 1


print(r)

# part 2

def basin_fill(hm, basins, basin, i, j):
    if basins[i][j] != -1:
        return 0
    
    if hm[i][j] == 9:
        return 0
    
    basins[i][j] = basin
    
    s = 1
    
    if j-1 >= 0 and hm[i][j] < hm[i][j-1]:
        s += basin_fill(hm, basins, basin, i, j-1)
    if j+1 < m and hm[i][j] < hm[i][j+1]:
        s += basin_fill(hm, basins, basin, i, j+1)
    if i-1 >= 0 and hm[i][j] < hm[i-1][j]:
        s += basin_fill(hm, basins, basin, i-1, j)
    if i+1 < n and hm[i][j] < hm[i+1][j]:
        s += basin_fill(hm, basins, basin, i+1, j)
    
    return s

b = [[-1] * m for _ in range(n)]

mx = [0]*3

bn = 1

for i in range(n):
    for j in range(m):
        if hm[i][j] == 9:
            continue
        if low(hm, i, j):
            t = basin_fill(hm, b, bn, i, j)
            
            mx = mx + [t]
            mx.sort()
            mx = mx[1:]
            
            bn += 1
            
print(mx[0] * mx[1] * mx[2])

