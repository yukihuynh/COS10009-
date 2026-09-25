line = int(input("How many lines are you entering? "))
def read_array():
    i = 0 
    list = []
    while i < line: 
        text = str(input("Enter text: "))
        list.append(text)
        i += 1
    return list
    
def print_array(list):
    index = 0 
    print("Printing lines:")
    while index < line:
        print(f"{index}. {list[index]}")
        index += 1
    
def main():
    my_list = read_array()
    print_array(my_list)
if __name__ == "__main__":
    main()