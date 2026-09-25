import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello {name}!")

window = tk.Tk()
window.title("Greeting App")

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Greet", command=greet)
button.pack(pady=5)

label = tk.Label(window, text="")
label.pack(pady=10)

window.mainloop()