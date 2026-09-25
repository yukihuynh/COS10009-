from enum import Enum

class Month(Enum): 
    January = 1

m = Month.January

print(m)        # Month.January
print(m.name)   # January
print(m.value)  # 1

# use enum in a class
class Student: 
    def __init__(self, name: str, month: Month):
        self.name = name
        self.month = month
my_student = Student("Yuki",m)
print (f"{my_student} was borned in {m.value}")