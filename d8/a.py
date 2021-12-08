with open("in.txt") as f:
    s = [x for x in f.read().splitlines() if x != '']
    
v = [list(map(lambda x: [v for v in x.strip().split(' ')], line.split(' | '))) for line in s]

# part 1

c = 0
for l in v:
    for x in l[1]:
        if len(x) in [2, 4, 3, 7]:
            c += 1

print(c)

def common(a, b):
    return (a & b)

 
def fl(a, l):
    return next(set(x) for x in a if len(x) == l)

def flm(a, l):
    return [set(x) for x in a if len(x) == l]

# part 2

sum = 0
for l in v:
    k1 = fl(l[0], 2)
    k4 = fl(l[0], 4)
    k7 = fl(l[0], 3)
    k8 = fl(l[0], 7)
    
    a = list(k7 - k1)[0]
    upleft_and_middle = k4 - k1
    
    lower_left_bot = k8 - (k4 | k7)
    
    f5 = flm(l[0], 5)

    k2 = next(s for s in f5 if (s & lower_left_bot) == lower_left_bot)
    
    bot = list(next(s & lower_left_bot for s in f5 if len(s & lower_left_bot) == 1))[0]
    lower_left = list(lower_left_bot - set([bot]))[0]
    
    k2_and_k4 = k2 & k4
    
    middle = list(upleft_and_middle & k2_and_k4)[0]
    upleft = list(upleft_and_middle - set([middle]))[0]
    
    k3 = next(s for s in f5 if s & k1 == k1)
    
    k5 = next(s for s in f5 if s != k2 and s != k3)
    
    k9 = k8 - set([lower_left])
    k0 = k8 - set([middle])
    k6 = next(s for s in flm(l[0], 6) if s != k9 and s != k0)
    
    k = [k0, k1, k2, k3, k4, k5, k6, k7, k8, k9]
    
    d1 = set(l[1][0])
    d2 = set(l[1][1])
    d3 = set(l[1][2])
    d4 = set(l[1][3])
    
    d1 = k.index(d1)
    d2 = k.index(d2)
    d3 = k.index(d3)
    d4 = k.index(d4)
    
    sum += d1 * 1000 + d2 * 100 + d3 * 10 + d4

print(sum)