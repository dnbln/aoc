with open("in.txt") as f:
    s = f.read()

v = [x.split(' ') for x in s.splitlines() if x != '']
x = 0
d = 0
for el in v:
    if el[0] == 'forward':
            x += int(el[1])
    elif el[0] == 'up':
            d -= int(el[1])
    elif el[0] == 'down':
            d += int(el[1])

print(x * d)

x = 0
d = 0
aim = 0

for el in v:
    if el[0] == 'up':
        aim -= int(el[1])
    elif el[0] == 'down':
        aim += int(el[1])
    elif el[0] == 'forward':
        p = int(el[1])
        x += p
        d += p * aim

print(x * d)
