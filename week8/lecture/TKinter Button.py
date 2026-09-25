import tkinter as tk 

def on_button_click():
    label.config(text="button clicked")

window = tk.Tk()
window.title("Event Loop example")
window.geometry("300x150")

label = tk.Label(window, text="Click the button")
label.pack(pady=10)

button = tk.Button(window, text="click me", command=on_button_click)
button.pack()

window.mainloop()