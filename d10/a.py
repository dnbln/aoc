with open("in.txt") as f:
    s = f.read()
    
def parse(s):
    return [x for x in s.splitlines() if x != '']

v = parse(s)

# part 1

score = 0

incomplete = []

for l in v:
    sck = []
    good = True
    for p in l:
        if p == '(':
            sck.append('(')
        elif p == '[':
            sck.append('[')
        elif p == '{':
            sck.append('{')
        elif p == '<':
            sck.append('<')
        elif p == ')':
            if sck[-1] != '(':
                score += 3
                good = False
                break
            sck = sck[:-1]
        elif p == ']':
            if sck[-1] != '[':
                score += 57
                good = False
                break
            sck = sck[:-1]
        elif p == '}':
            if sck[-1] != '{':
                score += 1197
                good = False
                break
            sck = sck[:-1]
        elif p == '>':
            if sck[-1] != '<':
                score += 25137
                good = False
                break
            sck = sck[:-1]
    if good:
        incomplete.append((l, sck))

print(score)

# part 2
# setup from part 1 with incomplete list

scores = []

for l, sck in incomplete:
    i = len(sck)-1
    scr = 0
    while i >= 0:
        if sck[i] == '(':
            scr = scr * 5 + 1
        elif sck[i] == '[':
            scr = scr * 5 + 2
        elif sck[i] == '{':
            scr = scr * 5 + 3
        elif sck[i] == '<':
            scr = scr * 5 + 4
        i -= 1
    scores.append(scr)

scores.sort()

print(scores[len(scores)//2])
