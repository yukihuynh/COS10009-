import input_functions


# ===============================
# Input list function
# ===============================
def input_number_list():
    numbers = []
    count = input_functions.read_integer_in_range("How many numbers do you want to enter?", 1, 100)

    i = 0
    while i < count:
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)
        i += 1

    return numbers


# ===============================
# Processing functions
# (return only, no print)
# ===============================
def total_list(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total


def average_list(numbers):
    return total_list(numbers) / len(numbers)


def search_list(numbers, target):
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            return True
        i += 1
    return False


# ===============================
# List Processing Sub Menu
# ===============================
def list_processing_menu():
    finished = False
    numbers = []

    while finished == False:
        print("\nList Processing Menu:")
        print("1 Enter a list of numbers")
        print("2 Calculate total of the list")
        print("3 Calculate average of the list")
        print("4 Search for a value in the list")
        print("5 Return to Main Menu")

        choice = input_functions.read_integer_in_range("Please enter your choice:", 1, 5)

        match choice:
            case 1:
                numbers = input_number_list()

            case 2:
                if len(numbers) == 0:
                    print("The list is empty. Please enter a list first.")
                else:
                    print("The total of the elements is", total_list(numbers))
                input("Press Enter to continue")

            case 3:
                if len(numbers) == 0:
                    print("The list is empty. Please enter a list first.")
                else:
                    print("The average of the elements is", average_list(numbers))
                input("Press Enter to continue")

            case 4:
                if len(numbers) == 0:
                    print("The list is empty. Please enter a list first.")
                else:
                    value = float(input("Enter a value to search for: "))
                    if search_list(numbers, value):
                        print(value, "was found in the list.")
                    else:
                        print(value, "was not found in the list.")
                input("Press Enter to continue")

            case 5:
                finished = True

            case _:
                print("Please select again")


# ===============================
# Option 2 – Other Feature (Stub)
# ===============================
def other_feature():
    print("You selected Option 2 (Other Feature).")
    input("Press Enter to return to the Main Menu")


# ===============================
# Main Menu (Ruby-style)
# ===============================
def main():
    finished = False

    while finished == False:
        print("\nMain Menu:")
        print("1 List Processing")
        print("2 Other Feature")
        print("3 Exit")

        choice = input_functions.read_integer_in_range("Please enter your choice:", 1, 3)

        match choice:
            case 1:
                list_processing_menu()
            case 2:
                other_feature()
            case 3:
                finished = True
            case _:
                print("Please select again")


main()
