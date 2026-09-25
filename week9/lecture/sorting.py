import random

messy_list = [random.randint(1,100) for _ in range (1,20)]

print(messy_list)

print (messy_list.sort()) # this will give you none and you shouldn't be using the code like this !!!!!

messy_list.sort() # we need sperate line for this
print(messy_list) # end then we're good to print out

print(sorted(messy_list, reverse=True)) #Reverse the order of the list, sorted takes an iterable and returns the sorted one


