class Student: 
    def __init__(self, name, age, rollNum):
        self.name = name 
        self.age = age 
        self.rollNum = rollNum

p1 = Student("John", 20, 1)
p2 = Student("Harry", 22, 2)
p3 = Student("Peter", 21, 3)
print(p1.name)
print(p1.age)
print(p1.rollNum)

print(p2.name)
print(p2.age)
print(p2.rollNum)

print(p3.name)
print(p3.age)
print(p3.rollNum)