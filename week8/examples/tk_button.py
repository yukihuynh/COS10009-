import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

window = tk.Tk()
window.title("Button Example")

label = tk.Label(window, text="Click the button")
label.pack(pady=10)

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

window.mainloop()