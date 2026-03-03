class Person:
    def __init__(self, name, age = 22):
        self.name = name
        self.age = age
    def self_intro(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")


p1 = Person("sato", 38)
p1.self_intro()