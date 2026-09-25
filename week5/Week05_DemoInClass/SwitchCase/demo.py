def main():
    value = 2

    match value:
        case 1:
            result = "one"
        case 2:
            result = "two"
        case 3:
            result = "three"
        case _:
            result = "unknown"

    print(result)  # Output: two
# end main

main()