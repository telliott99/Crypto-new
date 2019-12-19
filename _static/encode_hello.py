lc = 'abcdefghijklmnopqrstuvwxyz'
D = dict(zip(lc,range(1,len(lc)+1)))
D[" "] = 0


s = 'hello world'
m = 0
N = 27
for i,c in enumerate(s):
    m += D[c] * N**i

print(m)


rD = dict(zip(D.values(),D.keys()))
pL = list()
while m:
    pL.append(rD[m % N])
    m /= N
print(''.join(pL))
