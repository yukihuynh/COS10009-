import input_functions

# ===============================
# List Processing Sub Menu
# ===============================
def list_processing_menu():
    finished = False

    while finished == False:
        print("\nList Processing Menu:")
        print("1 Enter a list")
        print("2 Calculate total")
        print("3 Calculate average")
        print("4 Search in list")
        print("5 Return to Main Menu")

        choice = input_functions.read_integer_in_range("Please enter your choice:", 1, 5)

        match choice:
            case 1:
                enter_list()
            case 2:
                calculate_total()
            case 3:
                calculate_average()
            case 4:
                search_item()
            case 5:
                finished = True
            case _:
                print("Please select again")


# ===============================
# Stub functions (EXPLANATION ONLY)
# ===============================
def enter_list():
    print("This is the code for ENTERING a list.")
    input("Press Enter to continue")


def calculate_total():
    print("This is the code for CALCULATING the total of a list.")
    input("Press Enter to continue")


def calculate_average():
    print("This is the code for CALCULATING the average of a list.")
    input("Press Enter to continue")


def search_item():
    print("This is the code for SEARCHING an item in a list.")
    input("Press Enter to continue")


# ===============================
# Option 2 – Other Feature (Stub)
# ===============================
def other_feature():
    print("This is the code for OPTION 2 in the Main Menu.")
    input("Press Enter to continue")


# ===============================
# Main Menu
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
