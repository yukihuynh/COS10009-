listIndex = [0, 1, 2, 3]
listNames: list[str] = ["Bob", "Susie", "Randy", "Krog the Destroyer"]
listNum: list[int] = [10, 23, 9, 34]

print(*listIndex, sep='       ')
print(listNames)
print(*listNum, sep='       ')

listNames[3] = "Krog the Accountant"
print(listNames)

listDupes = ["Dog", "Cat", "Rabbit", "Cat", "Cat"]

print(type(listNames))
print(type(listNum))