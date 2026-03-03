class Person:
    def __init__(self, name, age = 22):
        self.name = name
        self.age = age


p1 = Person("itou")
print(p1.name)
print(p1.age)