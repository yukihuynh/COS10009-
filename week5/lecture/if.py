for hour in range(24):
    for min in range (60):
        for sec in range (60):
            print(f"{hour}:{min}:{sec}")

for i in range(10):
    if i == 5: 
        continue    # this will ignore the number 5 and continue with the rest of the
    print(i)