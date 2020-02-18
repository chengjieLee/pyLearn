import functools

int16 = functools.partial(int, base=16)

print(int16('10086'))