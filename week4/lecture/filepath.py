#open file 

# sử dụng w mode thì các phần write trước đó sẽ bị xóa đi. Trừ khi dùng 'a' mode thì sẽ vãn giữ lại !!

my_file_path = './lecture/file_demo.txt'
my_file = open(my_file_path,"w")
my_file.write("hello\n")
my_file.write("World\n")
my_file.write("!\n")

my_file = open(my_file_path, "a")
my_file.write("I\n")
my_file.write("am\n")
my_file.write("silly\n")
my_file.write("silly\n")
my_file.write("duck\n")

my_file = open(my_file_path,"w")
my_file.write("This has been changed")

#use close to save the file
my_file.close()
