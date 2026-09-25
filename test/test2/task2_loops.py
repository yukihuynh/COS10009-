def main():
    # put your code here
    index = 0 
    total = 0
    while index < 10:
        num = (int(input(f"Enter an integer: ")))
        total += num
        index += 1
    print(f"Total is: {total}")
if __name__ == "__main__":
    main()