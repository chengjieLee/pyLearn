# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s ： %s' % (self.name, self.score))

# xm = Student('xm',55)

# xm.print_score()

class Student(object):
    count = 0
    def __init__(self, name, age):
        Student.count += 1
        self.name = name
        self.age = age
    def get_count(self):
        return self.count
print(Student.count)
xm = Student('xm',22)
print(xm.count)

xf = Student('xf',21)

print(xf.count)