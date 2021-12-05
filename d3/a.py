with open("in.txt") as f:
    s = f.read()

v = [x for x in s.splitlines() if x != '']

gam = ''
eps = ''

for val in range(len(v[0])):
    f = [0, 0]
    for p in v:
        f[int(p[val])] += 1

    if f[0] > f[1]:
        gam += '0'
        eps += '1'
    else:
        gam += '1'
        eps += '0'

print(int(gam, 2) * int(eps, 2))

rem_ox = v.copy()
rem_co2 = v.copy()

for val in range(len(v[0])):
    f = [0, 0]
    for p in rem_ox:
        f[int(p[val])] += 1

    if f[0] > f[1]:
        bvox = '0'
    elif f[0] == f[1]:
        bvox = '1'
    else:
        bvox = '1'

    i = 0
    while i < len(rem_ox):
        if len(rem_ox) == 1:
            break

        if rem_ox[i][val] != bvox[0]:
            rem_ox.pop(i)
            i -= 1

        i += 1

for val in range(len(v[0])):
    f = [0, 0]
    for p in rem_co2:
        f[int(p[val])] += 1

    if f[0] > f[1]:
        bvco2 = '1'
    elif f[0] == f[1]:
        bvco2 = '0'
    else:
        bvco2 = '0'

    i = 0
    while i < len(rem_co2):
        if len(rem_co2) == 1:
            break

        if rem_co2[i][val] != bvco2[0]:
            rem_co2.pop(i)
            i -= 1

        i += 1

print(int(rem_ox[0], 2) * int(rem_co2[0], 2))
