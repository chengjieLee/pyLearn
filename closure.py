def createCounter():
    arr = [0]
    def counter():
        arr[0] = arr[0] + 1
        return arr[0]
    return counter

count = createCounter()
print(count(),count(),count())

# 与js区别
# def createCounter():
#     num = 0
#     def counter():
#         num = num + 1
#         return num
#     return counter

# count = createCounter()
# print(count(),count(),count())
# UnboundLocalError: local variable 'num' referenced before assignment

