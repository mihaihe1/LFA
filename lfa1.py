def parcurgere(st, s):
    ch = s[0]
    global ok
    for i in range(1,n+1):
        if (st, i) in d:
            if ch in d[(st, i)]:
                sir2 = s[1:]
                if sir2 == '':
                    if i in final:
                        ok = 1
                else:
                    parcurgere(i, s[1:])

#d = {(1,1):4,(1,2):['a','b']}
d = {}
f = open("date.in", "r")
x = f.readline().split()
n = int(x[0])
m = int(x[1])
for i in range(m):
    t = f.readline().split()
    x = int(t[0])
    y = int(t[1])
    c = t[2]
    if (x, y) in d:
        d[(x, y)].append(c)
    else:
        d[(x, y)] = []
        d[(x, y)].append(c)

sir = f.readline().rstrip("\n")
cnt = 0
#print(sir)
sirc = []
for i in sir:
    if i != '0':
        sirc.append(i)
sir = "".join(sirc)
#print(sir)
start = int(f.readline())
final = [int(x) for x in f.readline().split()]
ok = 0
if sir != '':
    parcurgere(start, sir)
else:
    if start in final:
        ok = 1

if ok == 1:
    print("DA")
else:
    print("NU")
f.close()