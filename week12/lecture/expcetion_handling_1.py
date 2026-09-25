while True:
    filename = input("Enter filename: ")
    try:
        f = open(filename)

    except FileNotFoundError:
        print("Failed to open", filename)
        print("Please re-enter")

    else:
        print("Successfully opened", filename)
        content = f.read()
        break

    finally:
        print("Codes put here will run every time")
