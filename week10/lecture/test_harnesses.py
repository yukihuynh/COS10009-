import input_functions 


class GemRecord:
    def __init__(self, id, description, weight, price):
        self.id = id
        self.description = description
        self.weight = weight
        self.price = price

# Defensive Programming approach
def display_gem(gem):
    print("Gem information is:")
    print(int(gem.id))
    print(gem.description if gem.description is not None else "Unknown")
    print(f"{gem.weight:.2f}")
    print(f"${gem.price:.2f}")


#The original
# def display_gem(gem):
#     print("Gem information is:")
#     print(gem.id)
#     print(gem.description)
#     print(gem.weight)
#     print(gem.price)


# Validation approach 
# def read_gem():
#     id = input_functions.read_integer("Enter ID: ")
#     description = input_functions.read_string("Enter description: ")
#     weight = input_functions.read_float("Enter weight (g): ")
#     gprice = input_functions.read_float("Enter price (AUD): ")
#     return GemRecord(id, description, weight, gprice)

#This serves for GOlden Rule Testing
def display_gems(gems):
    index = 0
    while index < len(gems):
        display_gem(gems[index])
        index += 1

def main():
    # Defensive programming
    # Test 1 – Normal input
    test_gem = GemRecord(1, "Emerald", 4, 580.99)  #local v
    print("Test 1 Output:")
    display_gem()

    # Test 2 – Edge cases
    test_gem = GemRecord(2.9, None, 4.568, 580.99)
    print("Test 2 Output:")
    display_gem(test_gem)

    #Test 3 = 
    test_gem = GemRecord(3, "Ruby" , 6.9, 799.9)
    print("Test case 3")
    display_gem(test_gem)

    #test 4
    test_gem = GemRecord(5.6, "Chair" ,3.4, 2)
    print ("Test 4")
    display_gem(test_gem)

    #Validation approach
    # test_gem = read_gem()
    # print("Test 1 Output:")
    # display_gem(test_gem)
    
main()


