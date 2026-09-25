import tkinter as tk
import random

def roll_dice():
    number = random.randint(1, 6)
    label.config(text=f"You rolled: {number}")

window = tk.Tk()
window.title("Dice Roller")

button = tk.Button(window, text="Roll Dice", command=roll_dice)
button.pack(pady=10)

label = tk.Label(window, text="Roll the dice!")
label.pack(pady=10)

window.mainloop()