numbers = list(range(1,15))
print(numbers)
# Gets all the elements (x) in numbers only if they're divisible by 2.
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Get all the elements (x) multiplied by 2 in numbers.
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)
