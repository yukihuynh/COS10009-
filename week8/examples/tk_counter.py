import tkinter as tk

count = 0

def increase_count():
    global count
    count += 1
    label.config(text=f"Clicks: {count}")

window = tk.Tk()
window.title("Click Counter")

label = tk.Label(window, text="Clicks: 0")
label.pack(pady=10)

button = tk.Button(window, text="Click", command=increase_count)
button.pack()

window.mainloop()