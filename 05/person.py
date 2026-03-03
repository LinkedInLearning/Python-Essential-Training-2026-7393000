class Person:
    def __init__(self, name, age = 22):
        self.name = name
        self.age = age
    def self_intro(self):
        print("My name is {0}. I'm {1} years old.".format(self.name,self.age))