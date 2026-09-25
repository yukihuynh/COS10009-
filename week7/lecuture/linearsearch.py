my_num = [1,2,3,4,5,6,7,8,9,10]
target = 9
def linersearch (list,target):
    n = len(list) 
    for i in range (0, n - 1):
        if list[i] == target: 
            return i 
    return - 1
output = linersearch(my_num, target)
print(f"THe ouput is {output}")

def change(x):
    x = 10 
a = 5
change(a)
print(a)