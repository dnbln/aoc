with open("in.txt") as f:
    s = f.read()
    
def parse(s):
    return [x.split('-') for x in s.splitlines() if x != '']
    
def iup(s):
    return all('A' <= x <= 'Z' for x in s)

G = parse(s)

d = {}

for e in G:
    try:
        d[e[0]].append(e[1])
    except KeyError:
        d[e[0]] = [e[1]]
        
    try:
        d[e[1]].append(e[0])
    except KeyError:
        d[e[1]] = [e[0]]

def cnt(d, pos, cs):
    if pos == 'end':
        return 1
    p = len(cs)
    
    if (not iup(pos)) and pos in cs:
        return 0
    cs.append(pos)
    
    total = 0
    
    for v in d[pos]:
        total += cnt(d, v, cs)
    
    cs.pop(p)
    
    return total

print(cnt(d, 'start', []))

def cnt2(d, pos, cs, sc2 = None):
    if pos == 'end':
        return 1
    
    p = len(cs)
    
    rsc2 = sc2
    
    if (not iup(pos)):
        if pos in cs:
            if rsc2 == None:
                rsc2 = pos
            else:
                return 0
    cs.append(pos)
    
    total = 0
    
    for v in d[pos]:
        if v == 'start':
            continue
        total += cnt2(d, v, cs, rsc2)
    
    cs.pop(p)
    
    return total

print(cnt2(d, 'start', []))