def main(): 
    print_name("Yuki",20)
    calculate_circle_area (20)
    student_email ("Yuki")

#this is a procedure
def print_name(name, age):
    print (f" Tôi tên {name} và tôi {age} tuổi")
    #doesm't return value

def calculate_circle_area (radius): 
    area =  radius ** 2 * 3.14
    return area 
# any lines come after return will be ignored ! 

def student_email (name): 
    return f"{name}@swin.edu.au"

main()


