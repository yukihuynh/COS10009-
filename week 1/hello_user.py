from datetime import date

INCHES = 39.3701  # This is a global constant

# Insert the missing code here into the statements below:
# input()
# input().strip()
# date.today().year
# int(year_born)
# float(input())

def hello():
    name = str(input("Please enter your name:"))
    print("Your name is " + name + "!")

    print("Please enter your family name:")
    family_name = input().strip()
    print("Your family name is " + family_name + "!")

    print("Please enter your year of birth:")
    year_born = int(input())

    # Calculate the user's age
    age = date.today().year - int(year_born)
    print("So you are " + str(age) + " years old")

    print("Enter your height in metres (i.e as a float):")
    value =  float(input())# Should this be a float or an Integer? Why?
    value = value * INCHES

    print("Your height in inches is:")
    print("{:.2f}".format(value))   
    print("Finished")


def main():
    hello()


if __name__ == "__main__":
    main()
