# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n * fact(n-1)

# ind = fact(10)
# print(ind)

def trimLetf(str):
    ind = -1
    for i in str:
        if i ==' ':
            ind +=1
        else:
            break
    return str[ind+1:]

print(trimLetf('    a in'))

def trim(str):
    ind1 = 0
    ind2 = len(str)-1
    while str[ind1] == ' ':
        ind1 = ind1+1
    while str[ind2] ==' ':
        ind2 = ind2-1
    return str[ind1:ind2+1]

print(trim('  hh  12  '), len(trim('  hh  12 ')),' 111  '.strip())

#下标循环
for i, value in enumerate(['A','B','C']):
    print(i,value)

# 双参数循环
for a,b in [(1,3),(2,4),(3,5)]:
    print(a,b)
