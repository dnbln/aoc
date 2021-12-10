with open("in.txt") as f:
    v = [int(x) for x in f.readlines()[0].split(',')]

# part 1

def comp(v, p):
    return sum(abs(x - p) for x in v)

p = 0
while comp(v, p) > comp(v, p+1):
    p = p + 1

print(comp(v,p))

# part 2

def comp2(v, p):
    return sum(abs(x-p) * (abs(x-p) + 1) // 2 for x in v)

p = 0
while comp2(v,p) > comp2(v, p+1):
    p = p+1

print(comp2(v,p))