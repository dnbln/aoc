with open("in.txt") as f:
    s = f.read()
v = [int(x) for x in s.splitlines() if x != '']

# part 1
count = 0
for i in range(len(v)):
    if i > 0 and v[i] > v[i-1]:
        count = count + 1

print(count)

# part 2
count = 0
for i in range(len(v)):
    if i >= 3 and v[i] > v[i-3]:
        count = count + 1

print(count)
