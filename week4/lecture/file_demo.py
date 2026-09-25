#open the file
file_path = './lecture/file_demo.txt'

my_file = open(file_path, "r")
#read()

#use this if the file is short
#my_file_content = my_file.read()
#print(my_file_content)

#readlines()
#use this if you're confident with list opearations
#my_lines = my_file.readlines()
#print(my_lines)


#strip method will get rid of very space "/n" !!
#my_line = my_file.readline().strip()
#print(my_line)

#for loop
#for index in range(10):
    #print(index)
for line in my_file:
    print(line.strip())


#while loop 
#index = 0 
#while (index <10):
    #print(index)
    #index += 1

my_line = my_file.readline().strip() #print out first "name"
while (my_line !=''):           #my_line không bằng rỗng thì nó sẽ print ra my_line là các tên trong txt 
    print(my_line)
    my_line = my_file.readline().strip() # ở đây sẽ tiếp tục lặp lại quá trình print my_line cho đến khi nó rỗng thì nó sẽ tự thoát chương trình. 
