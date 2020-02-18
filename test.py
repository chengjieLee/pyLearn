import random # 随机数
# and === &&
#  or === ||
# name = input('请输入第一个数字')
# age = input('第二个')

# print(random.randrange(5,10)+int(name)*int(age))
# arr = ['he','hi','her']

# print(arr)
# s3 = r'Hello,"bart"' # r 标识 用来把后面定义的字符串不做转义
# print(s3)
# x = range(101)
# sum = 0
# for i in x:
#     sum += i
# print(sum)

#无限循环
# x = 1
# while x > 0:
#     x = x+1
#     print(x)

# dictionary
# dic = {'a':10,'b':20,'c':33}

# print(dic['a'], 'b' in dic)
# list = [7,8,1,5,9]
# print(max(list))
# ┌────────────────────────────────────────────────────────┐
import math

def quadratic(a,b,c):
    drt = b*b - 4*a*c
    if(drt < 0):
        return '方程无解'

    x1 = (-b+math.sqrt(drt))/2*a
    x2 = (-b-math.sqrt(drt))/2*a
    if(x1 != x2):
        return x1, x2
    else:
        print('该方程只有一个解')
        return x1

# 3X^2 + 2x +3 = 0
print(quadratic(-3,2,3))

def func (a,b=1,*c,**d):
    pass
# a: 必选参数   b: 带有默认值 *c 可变参数列表 tuple(元组) 例：m,n **d 可变参数dict 例: x=1,y=2