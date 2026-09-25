# When we use Immutable Data like an int it doesn't change the value outside the function.
def change(x):
    x = 10

a = 5
change(a)
print(a)

# However for a list any changes made to the list are permanent outside of the function.
def changeMutable(lst):
    lst.append(4)

numbers = [1, 2, 3]
changeMutable(numbers)
print(numbers)