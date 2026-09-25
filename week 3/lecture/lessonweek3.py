class Student: 
    #constructor - self refer to class it self (Student)
    #self is not parameter
    def __init__(self, name:str, id:str, age: int):
        self.name = name  
        self.stu_id = id
        self.stu_age = age 
    
    def print_detail(self):
        print (f"The student information is {self.name} - {self.stu_id}. He/she is {self.stu_age} years old "
)

#create instance of the class / object
my_student1 = Student ("Alex", "SWS1215", 18)
my_student2 = Student ("Yuki", "SWS01951", 18 )

#print out student information
#print (                           
#    f"The student information is {my_student.name} - {my_student.stu_id}. He/she is {my_student.stu_age} years old ")

