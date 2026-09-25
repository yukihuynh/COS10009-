data = [6, -3, 3, 8, 1]

def whatdoesFunctiondo(data): 
    result = 0 
    i = 0 
    while i < len(data): 
        result = result + data[i]
        i = i + 1
    return result

# Call the function
print(whatdoesFunctiondo(data))