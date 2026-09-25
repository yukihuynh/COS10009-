

def sum(num1,num2):
    return num1 + num2

total = sum(1,3)
print(total)

def get_name():
# Get the user’s first and last name.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
# Return both names.
    return first, last

hi = get_name()
print (hi)  