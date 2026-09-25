import tkinter as tk 

count= 0 

def increse_count():
    global count
    count += 1 
    label.config(text=f"ClicksL {count}")

window = tk.Tk()
window.title("Click Counter")

label = tk.Label(window, text="Clicks: 0")
label.pack(pady=10)

button = tk.Button(window, text="Click", command= increse_count)
button.pack()

window.mainloop()