try:
    txt = open('./test.txt','r')
    txtStr = txt.read()
    print(txtStr)
finally:
    if txt:
        txt.close()


with open('./test.html', 'r') as ht:
    for line in ht.readlines():
        print(line.strip())

with open('./test.txt', 'a') as tx:
    tx.write('nice')