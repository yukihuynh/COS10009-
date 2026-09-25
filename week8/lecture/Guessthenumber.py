import tkinter as tk
import random 

number = random.randint(1,10)
def guess(): 
    global number
    guess = int(entry.get())
    if guess == number:
        label.config(text=f"Correct! The number is {number}")
    elif guess > number:
        label.config(text=f"The number your guess is lower than the answer")
    elif guess < number:
        label.config(text=f"The number your guess is higher than the answer")

window = tk.Tk()
window.title("Entering a Number")

label = tk.Label(window, text="Enter a number")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Submit Num", command=guess)
button.pack(pady=10)

window.mainloop()