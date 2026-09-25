import tkinter as tk

# Event handler function
def on_button_click():
    label.config(text="Button was clicked!")

# Create window
window = tk.Tk()
window.title("Event Loop Example")
window.geometry("300x150")

# Create label
label = tk.Label(window, text="Click the button")
label.pack(pady=10)

# Create button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Start the event loop
window.mainloop()