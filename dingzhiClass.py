class Ch():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Ch object name is %s' % self.name
    __repr__ = __str__


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if(self.a > 1000):
            raise StopIteration()
        return self.a

for i in Fib():
    print(i)