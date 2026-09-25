# #1Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z if the
# variable x is greater than 100.
y =0 
z= 0 
x = 100
if x >= 100: 
    print("1. x is equal to 100 so:")
    y +=20 
    z +=40
    print(f"Y is {y} and z is {z}\n" )

# 2. Write an if statement that assigns 10 to the variable b and 50 to the variable c if the variable a
# is equal to 100.
A = 100
B = 0
C = 0
if A >=100: 
    print("2. A is equal to 100 so:")
    B +=10 
    C +=50
    print(f"B is {B} and C is {C}\n" )

# 3. Write an if-else statement that assigns 0 to the variable b if the variable a is less than 10.
# Otherwise, it should assign 99 to the variable b.
a = int(input("Enter value of A: "))
b = 0
if a < 10: 
    print (f"b equal to {b}\n")
else: 
    print (f"b equal to {b + 99}\n")

# 4. The following code contains several nested if-else statements.
# Unfortunately, it was written without proper alignment and indentation.
# Rewrite the code and use the proper conventions of alignment and indentation.

# if score >= A_score:
#     print('Your grade is A.')
# elif score >= B_score:
#     print('Your grade is B.')
# elif score >= C_score:
#     print('Your grade is C.')
# elif score >= D_score:
#     print('Your grade is D.')
# else:
#     print('Your grade is F.')

# 5. Write nested decision structures that perform the following: If amount1 is greater than 10 and
# amount2 is less than 100, display the greater of amount1 and amount2.
import random 
amount1 = random.randint(10,100)
amount2 = random.randint(0,100)
if amount1 > amount2: 
    print ("Amount1 is greater than amount2\n")
else: 
    print ("Amount2 is greater than amount1\n")

# 6. Write an if-else statement that assigns True to the again variable if the score variable is within
# the range of 40 to 49. If the score variable’s value is outside this range, assign False to the again
# variable.
score = int(input("Enter the score"))
if 40 <= score <= 49: 
    again = True
else: 
    again = False

# 7. Write an if-else statement that determines whether the points variable is outside the range of 9
# to 51. If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it
# should display “Valid points.
point = int(input("Enter the number:"))
if 9 <= point <= 51: 
    print ("Valid points.")
else: 
    print ("Invalid points.")

# 8. Write an if statement that uses the turtle graphics library to determine whether the turtle’s
# heading is in the range of 0 degrees to 45 degrees (including 0 and 45 in the range). If so, raise
# the turtle’s pen.
import turtle
if 0 <= turtle.heading() <= 45:
    turtle.penup()

# 9. Write an if statement that uses the turtle graphics library to determine whether the turtle’s pen
# size is greater than 1 or the pen color is red. If so, set the pen size to 1 and the pen color to blue.
if turtle.pensize() > 1 or turtle.pencolor() == "red":
    turtle.pensize(1)
    turtle.pencolor("red")

# 10. Write an if statement that uses the turtle graphics library to determine whether the turtle is
# inside of a rectangle. The rectangle’s upper-left corner is at (100, 100) and its lower-right corner
# is at (200, 200). If the turtle is inside the rectangle, hide the turtle.
x, y = turtle.pos()
if 100 <= x <= 200 and 100 <= x <= 200: 
    turtle.hideturtle()

#----------------------------------------------------------
#                               Loop

# 1. Write a while loop that lets the user enter a number. The number should be multiplied by 10,
# and the result assigned to a variable named product. The loop should iterate as long as product is
# less than 100
product = 0 
while product > 100: 
    number = int(input("Enter a number "))
    product = number * 10
    print (product)

# 2. Write a while loop that asks the user to enter two numbers. The numbers should be added and
# the sum displayed. The loop should ask the user if he or she wishes to perform the operation
# again. If so, the loop should repeat, otherwise it should terminate.
again = "y"
while again.lower() == "y":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print("Sum:", total)
    again = input("Do you want to perform the operation again? (y/n): ")

#3. Write a for loop that uses the range function to display all odd numbers between 1 and 100.
for num in range (1,100,2):
    print(num)

# 4. Starting with a variable text containing an empty string, write a loop that prompts the user to
# type a word. Add the user’s input to the end of text and then print the variable. The loop should
# repeat while the length of text is less than 10 characters.
while len(text) < 10:
    word = input("Enter a word: ")
    text += word
    print(text)
# 5. Write a loop that calculates the total of the following series of numbers:
total = 0
for i in range(1, 31):
    total += i / (31 - i)
print("Total:", total)