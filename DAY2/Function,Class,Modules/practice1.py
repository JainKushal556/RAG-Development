# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

print("Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.")
class Student:
    def __init__(self,name,eng,ben,math):
        self.name=name
        self.english=eng
        self.bengali=ben
        self.math=math

    def average_marks(self):
        return (((self.english+self.bengali+self.math)/3))
name = input("Name: ")
english = float(input("English Marks: "))
bengali = float(input("Bengali Marks: "))
math = float(input("Math Marks: "))

s1 = Student(name,english,bengali,math)
print("Name: "+ s1.name)
print("Avreage: "+ str(f"{s1.average_marks():.2f}"))
