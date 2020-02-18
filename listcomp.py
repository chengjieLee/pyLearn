L1 =['Hello', 'World', 32, 'Apple', None]

L2 = [x.lower() for x in L1 if(isinstance(x, str))]
#对每一项结果操作 |循环       |判断条件
# print(L2)

L3 = ['ADm','AtM','helLo']

def Upper(s):
    i=0
    y=''
    while i < len(s):
        if i==0:
            y = s[i].upper()
        else:
            y += s[i].lower()
        i = i + 1
    return y

print(list(map(Upper, L3)))



