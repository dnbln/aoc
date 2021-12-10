with open("in.txt") as f:
    s = f.read()

v = [int(x) for x in s.splitlines()[0].split(',')]

vc = v.copy()

for d in range(1, 81):
    l = len(v)
    for i in range(l):
        if v[i] == 0:
            v[i] = 6
            v.append(8)
        else:
            v[i] -= 1

print(len(v))

v = vc
dv = [0] * (256 + 1)

for x in v:
    dv[1+x] += 1

l = len(v)

for d in range(1, 256 + 1):
    if d + 9 <= 256:
        dv[d + 9] += dv[d] # new spawn
    if d + 7 <= 256:
        dv[d + 7] += dv[d] # spawn
    l += dv[d]

print(l)
