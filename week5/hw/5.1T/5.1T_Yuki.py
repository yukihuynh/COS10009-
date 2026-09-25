from input_functions import read_integer_in_range, read_string


# you could use the input functions instead of print and input

def display_albums():
    finished = False
    # complete this code to support the
    # menu options below - use the main menu code
    # to guide you.
    while finished == False:    
        print("Display Albums Menu:")
        print("1 Display All Albums")
        print("2 Display Albums by Genre")
        print("3 Return to Main Menu")

        choice = read_integer_in_range(
            "Please enter your choice: \n", 1, 3
        )
        match choice: 
            case 1: 
                display_all()
            case 2: 
                display_Genre()
            case 3:
                main()
            case _:
                print("Please select again")





# implement stub code for each option in the Display Albums menu

# this is stub code for main menu option 1
def load_albums():
    read_string("You selected Load Albums. Press Enter to continue\n")

def display_all(): 
    read_string("You selected Display All Albums . Press Enter to continue\n")

def display_Genre():
    read_string("You selected Load Albums By Genre. Press Enter to continue\n")

# complete the case statement below and
# add a stub like the one above for option 2
# of this main menu
def main():
    finished = False

    while finished == False:
        print("Main Menu:")
        print("1 Load Albums")
        print("2 Display Albums")
        print("3 Exit")

        choice = read_integer_in_range(
            "Please enter your choice:", 1, 3
        )

        match choice:
            case 1:
                load_albums()
            case 2:
                display_albums()
            case 3:
                finished = True
            case _:
                print("Please select again")


main()
