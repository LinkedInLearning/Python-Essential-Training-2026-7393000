from person import Person


class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age) 
        self.school = school
        self.grade = grade
    def self_intro(self):
        print(f"My name is {self.name}. I'm {self.grade} grade at {self.school} school.")


s1 = Student("yamaki", 15 ,"waseda", "first" )
s1.self_intro()