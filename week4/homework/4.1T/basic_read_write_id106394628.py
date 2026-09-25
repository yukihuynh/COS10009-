# writes the number of lines then each line as a string.

def write_data_to_file(a_file: str):
    a_file = open('./mydata.txt', "w")
    a_file.write("5\n")
    a_file.write("Fred\n")
    a_file.write("Sam\n")
    a_file.write("Jill\n")
    a_file.write("Jenny\n")
    a_file.write("Zorro\n")
    a_file.close()

# reads in each line.
# you need to change the following code
# so that it uses a loop which repeats
# according to the number of lines in the File
# which is given in the first line of the File
def read_data_from_file(a_file):
    a_file = open('./mydata.txt', "r")
    count = int(a_file.readline().strip())
    #print(str(count))
    for i in range(count):
        print(a_file.readline().strip())
    a_file.close()

# writes data to a file then reads it in and prints
# each line as it reads.
# you should improve the modular decomposition of the
# following by moving as many lines of code
# out of main as possible.
def main():
    a_file = "./mydata.txt"  # open for writing
    write_data_to_file(a_file)
    # a_file.close()    
    # a_file = open("./mydata.txt", "r")  # open for reading
    read_data_from_file(a_file)
    # a_file.close()
main()
