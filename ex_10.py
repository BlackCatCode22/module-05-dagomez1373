fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
       di[w] = di.get(w,0) + 1


tmp = dict()
newlist = list()
for k,v in di.items() :
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)

for v,k in cool[:5] :
    print(k,v)