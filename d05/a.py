with open("in.txt") as f:
    s = f.read()
    
def c(s):
    return [int(x) for x in s.split(',')]

txtlines = [x for x in s.splitlines() if x != '']
lines = [[c(x) for x in line.split(' -> ')] for line in txtlines]

maxx, maxy = (0, 0)

for l in lines:
    if l[0][0] > maxx:
        maxx = l[0][0]
    if l[1][0] > maxx:
        maxx = l[1][0]
    if l[0][1] > maxy:
        maxy = l[0][1]
    if l[1][1] > maxy:
        maxy = l[1][1]

def lf1(line):
    if line[0][0] == line[1][0]:
        return zip([line[0][0]] * 1001, range(line[0][1], line[1][1]+1) if line[0][1] <= line[1][1] else range(line[1][1], line[0][1]+1))
    elif line[0][1] == line[1][1]:
        return zip(range(line[0][0], line[1][0]+1) if line[0][0] <= line[1][0] else range(line[1][0], line[0][0]+1), [line[1][1]] * 1001)
    else:
        return None

def lf2(line):
    if line[0][0] == line[1][0]:
        return zip([line[0][0]] * 1101, range(line[0][1], line[1][1]+1) if line[0][1] <= line[1][1] else range(line[1][1], line[0][1]+1))
    elif line[0][1] == line[1][1]:
        return zip(range(line[0][0], line[1][0]+1) if line[0][0] <= line[1][0] else range(line[1][0], line[0][0]+1), [line[1][1]] * 1101)
    elif line[0][0] >= line[1][0]:
        if (line[0][0] - line[1][0]) == (line[0][1] - line[1][1]):
            return [(line[0][0]-d, line[0][1]-d) for d in range(line[0][0] - line[1][0] + 1)]
        elif (line[0][0] - line[1][0]) == -(line[0][1] - line[1][1]):
            return [(line[0][0]-d, line[0][1]+d) for d in range(line[0][0] - line[1][0] + 1)]
        else:
            return None
    elif line[0][0] < line[1][0]:
        if (line[0][0] - line[1][0]) == (line[0][1] - line[1][1]):
            return [(line[0][0]+d, line[0][1]+d) for d in range(-(line[0][0] - line[1][0]) + 1)]
        elif (line[0][0] - line[1][0]) == -(line[0][1] - line[1][1]):
            return [(line[0][0]+d, line[0][1]-d) for d in range(-(line[0][0] - line[1][0]) + 1)]
        else:
            return None
     

mat = [[0] * (maxx+1) for _ in range(maxy+1)]
tc = 0

for l in lines:
    lfx = lf1(l)
    if lfx:
        for x,y in lfx:
            mat[y][x] += 1

for l in mat:
    for x in l:
        if x >= 2:
            tc += 1
            
print(tc)

mat = [[0] * (maxx+1) for _ in range(maxy+1)]
tc = 0

for l in lines:
    lfx = lf2(l)
    
    if not lfx:
        continue
    
    lfx = list(lfx)
    for x,y in lfx:
        mat[y][x] += 1

for l in mat:
    for x in l:
        if x >= 2:
            tc += 1
            
print(tc)
