
class MyRecord():
    def __init__(self, name, age):
        self.name = name
        self.age = age  #fix1 

# Sort from largest to smallest age depending on direction
def compare(a, b, direction):
    result = True
    if a > b:
        result = True
    else:
        result = False

    if direction:
        return result
    else:
        return not result
    
# sort list according to direction
def sort(arr, direction):
    item_count = len(arr)
    # Now let's use bubble sort. Swap pairs iteratively as we loop through the
    # array from the beginning of the array to the second-to-last value
    for i in range(item_count - 1):
        # From arr[i + 1] to the end of the array
        for j in range(i + 1, item_count):
            if compare(arr[i].age, arr[j].age, direction):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    return arr

# Read the data from the file and print out each line
def read(aFile):
    people = []
    
    count = aFile.readline().strip()
    print(f'first line: {count}')
    if is_numeric(count):       #fix 2
        count = int(count)
    else:
        count = 0
        print('Error: first line of file is not a number')

    index = 0
    while index < count: #fix 3
        name = aFile.readline().strip()
        age = int(aFile.readline().strip())
        record = MyRecord(name, age)
        people.append(record)
        print('Line read: ', name)
        index += 1

    return people

def print_array(list):
    print(f'Printing list: number of elements: {len(list)}')
    i = 0
    while i < len(list):
        print(f'Name: {list[i].name} \n Age: {list[i].age}')
        i += 1

# Write data to a file then read it in and print it out
def main():
    aFile = open('data.txt', 'r') # open for writing
    people = read(aFile)
    aFile.close()

    sorted_people = sort(people, True)

    print_array(sorted_people)

# returns true if a string contains only digits
def is_numeric(obj):
    if obj.isnumeric():
        return True
    return False    
    
if __name__ == '__main__':
    main()