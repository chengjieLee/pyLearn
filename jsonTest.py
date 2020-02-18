import json

class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('xiaoM', 22, 88)

def class_to_dict(cls):
    return {
        'name': cls.name,
        'age': cls.age,
        'score': cls.score
    }
print(json.dumps(s, default=class_to_dict))
