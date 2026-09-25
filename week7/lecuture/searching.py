ages = [21, 16, 16, 34, 55, 11, 2, 34, 16, 55]
names = ["April", "Sam", "Oswold", "Bob"]

def linearSearch(inputList, target):
    for item in inputList:
        if item == target:
            return target
        
    return - 1

print(linearSearch(ages, 34))
print(linearSearch(ages, 99))
print("---------------------------------------------------")
print(linearSearch(names, "Sam"))
print(linearSearch(names, "Billy Mac"))

print("---------------------------------------------------")

# Easy python way
print(34 in ages)
print(99 in ages)
print("Sam" in names)
print("Billy Mac" in names)