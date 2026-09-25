def read_string(prompt):
    return input(prompt)

#Original
# def read_integer(prompt):
#     return int(read_string(prompt))

# Validation
def read_integer(prompt):
    value = read_string(prompt)
    while not value.isdigit():
        print("Please enter a whole number!")
        value = read_string(prompt)
    return int(value)

#Original
# def read_float(prompt):
#     return float(read_string(prompt))

#Validation
def read_float(prompt):
    value = read_string(prompt)
    while not value.replace(".", "", 1).isdigit():
        print("Please enter a number!")
        value = read_string(prompt)
    return float(value)


def read_integer_in_range(prompt, min_value, max_value):
    value = read_integer(prompt)
    while value < min_value or value > max_value:
        print(f"Please enter a value between {min_value} and {max_value}.")
        value = read_integer(prompt)
    return value


def read_boolean(prompt):
    value = read_string(prompt).lower()
    return value in ['y', 'yes']


def print_float(value, decimal_places):
    print(round(value, decimal_places))
