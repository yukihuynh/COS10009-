import random
from input_functions import read_integer_in_range

MIN = 1
MAX = 100

def main():
    r = random.randint(MIN, MAX)
    highest = MAX
    lowest = MIN
    guess = read_integer_in_range(f"Enter a number between {MIN} and {MAX}: ", MIN, MAX)
    while guess != r:
        if r > guess:
            lowest = guess
        else:
            highest = guess
        guess = read_integer_in_range(f"Enter a number between {lowest} and {highest}: ", lowest, highest)
    print("You guessed it!")

main()