class Enrollment: 
    def __init__(self, unit, attempt):
        self.stu_unit = unit 
        self.stu_attempt = attempt


class Student: 
    #constructor - self refer to class it self (Student)
    #self is not parameter
    def __init__(self, name: str, id: str, age: int, enrollment: Enrollment):
        self.name = name  
        self.stu_id = id
        self.stu_age = age 
        self.enrollment = enrollment
    
    def print_detail(self):
        print (f"The student information is {self.name} - {self.stu_id}. He/she is {self.stu_age} years old "
)

#nested class
my_student_enrollment = Enrollment ("Introducing Program", 3)
my_student = Student ("Yuki", "SWS01951", 18, my_student_enrollment)

print (f"The student {my_student.name} has tried to enrolled into {my_student_enrollment.stu_unit} {my_student_enrollment.stu_attempt} times")