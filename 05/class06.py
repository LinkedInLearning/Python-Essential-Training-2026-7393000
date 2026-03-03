from person import Person

class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age) 
        self.school = school
        self.grade = grade
    def self_intro(self):
        super().self_intro()
        print(f"I'm {self.grade} grade at {self.school} school.")

s1 = Student("yamaki", 15 ,"waseda", "first" )
s1.self_intro()