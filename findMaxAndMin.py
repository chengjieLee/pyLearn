def findMaxAndMin(list):
    if len(list)==0:
        max = None
        min = None
        return max,min
    else:
        max = list[0]
        min = list[0]
    for i in list:
        if i <= min:
            min = i
        if i > max:
            max = i
    return max,min

print(findMaxAndMin([-1,3,45,2]))
print(findMaxAndMin([7]))
print(findMaxAndMin([]))
