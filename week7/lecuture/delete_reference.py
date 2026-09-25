import sys
a = [1, 2, 3]
print("Reference count before:", sys.getrefcount(a))
b = a  # another reference to the same object
print("Reference count after assigning b:", sys.getrefcount(a))
del b  # delete one reference
print("Reference count after deleting b:", sys.getrefcount(a))

del a  # delete the final reference