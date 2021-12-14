with open("in.txt") as f:
    s = f.read()
    
def parse(s):
    lines = s.splitlines()
    fl = lines[0]
    rules = lines[2:]
    
    return list(fl), [rule.split(' -> ') for rule in rules if rule != '']

fl, r = parse(s)

def fr(ab, rules):
    for r in rules:
        if r[0] == ab:
            return r
            
    return None

def step(l, r):
    i = 0
    
    while i + 1 < len(l):
        rul = fr(l[i] + l[i+1], r)
        if rul:
            l = l[:i+1] + list(rul[1]) + l[i+1:]
            i += 1
        i += 1
        
    return l

cp = fl.copy()
for _ in range(10):
    cp = step(cp, r)


def ccmm(cp):
    counts = [0] * 128
    for s in cp:
        counts[ord(s)] += 1
        
    mx, mi = 0, ord(s[0])
    for i in range(128):
        if counts[i] > counts[mx]: mx = i
        if counts[i] != 0 and counts[i] < counts[mi]: mi = i
    
    return counts[mx] - counts[mi]

print(ccmm(cp))

def computed(l):
    i = 0
    d = {}
    while i + 1 < len(l):
        k = ''.join(l[i:i+2])
        try:
            d[k] += 1
        except KeyError:
            d[k] = 1
        i += 1
    
    fpair = ''.join(l[0:2])
    lpair = ''.join(l[-2:])
        
    return d, fpair, lpair

def step2(d, fpair, lpair, r):
    nd = {}
    for k in d:
        rul = fr(k, r)
        if rul:
            k1 = k[0] + rul[1]
            k2 = rul[1] + k[1]
            try:
                nd[k1] += d[k]
            except KeyError:
                nd[k1] = d[k]
                
            try:
                nd[k2] += d[k]
            except KeyError:
                nd[k2] = d[k]
        else:
            nd[k] = d[k]
            
    fprl = fr(fpair, r)
    if fprl:
        fp = fpair[0] + fprl[1]
    else:
        fp = fpair
        
    lprl = fr(lpair, r)
    if lprl:
        lp = lprl[1] + lpair[1]
    else:
        lp = lpair
        
    
    return nd, fp, lp

def mm(d, fp, lp):
    counts = [0] * 128
    for s in d:
        vl, vr = d[s], d[s]
        if s == fp:
            vl += 1
            
        if s == lp:
            vr += 1
            
        counts[ord(s[0])] += vl
        counts[ord(s[1])] += vr
    
    for i in range(128):
        counts[i] = counts[i] // 2
    
    mx, mi = 0, ord(s[0])
    for i in range(128):
        if counts[i] > counts[mx]: mx = i
        if counts[i] != 0 and counts[i] < counts[mi]: mi = i
    
    return counts[mx] - counts[mi]

d, fpair, lpair = computed(fl)

for stp in range(40):
    d, fpair, lpair = step2(d, fpair, lpair, r)

print(mm(d, fpair, lpair))