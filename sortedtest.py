from operator import itemgetter
L = [('bob',55),('xm',60),('nic',77),('nn',21)]

def by_src(t):
    return t[1]

M = sorted(L, key=itemgetter(1))
S = sorted(L, key=by_src)
R = sorted(L, key=lambda t: t[1])
print(M, '\n',S,'\n',R)