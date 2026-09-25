import input_functions as input_function 

def letter_label(title, first_name, last_name,  #function letter_label (title, first_name, last_name, unit_number, street_name, suburb, postcode)
                 unit_number, street_name,       #return all to f-string => end function 
                 suburb, postcode):
    return f"""{title} {first_name} {last_name}
{unit_number} {street_name}
{suburb} {postcode}"""

def letter_message(subject_line, message_content):      #function letter_message(subject_line, message_content)
                                                        # also return to f-string = end function
    return f"""RE: {subject_line}
{message_content}"""


def print_letter(label, message):   #function print_letter
    print(label)                #display label
    print()                     #display none
    print(message)              #display message


def main():         #main function 
    user_input_title = input_function.read_string("Please enter your title (Mr, Mrs, Ms, Miss, Dr): ")      #make a input for title

    user_input_first_name = input_function.read_string("Please enter your first name: ")            #make a input for first name

    user_input_last_name = input_function.read_string("Please enter your last name: ")              #make a input for last name

    user_input_unit_number = input_function.read_string("Please enter the house or unit number: ")  #make a input for unit number

    user_input_street_name = input_function.read_string("Please enter the street name: ")           #make a input for street name

    user_input_suburb = input_function.read_string("Please enter the suburb: ")                     #make a input for suburb

    user_input_postcode = input_function.read_integer_in_range(                                     #make a input for postcode with x in range from 0 to 9999
        "Please enter a postcode (0000 - 9999): ", 0, 9999)

    user_input_message_subject_line = input_function.read_string("Please enter your message subject line: ")   #make a input for subject line

    user_input_message_content = input_function.read_string("Please enter your message content: ")  #make a input for message content



    label = letter_label(   
        user_input_title,        #after return, make a label variable to stored details
        user_input_first_name,
        user_input_last_name,
        user_input_unit_number,
        user_input_street_name,
        user_input_suburb,
        user_input_postcode
    )

    message = letter_message(           #after return, make a message variable to stored details
        user_input_message_subject_line,
        user_input_message_content
    )

    print_letter(label, message)    #print out both variable 

main() #end function 
#end program

