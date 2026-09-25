import tkinter

# Named constants
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 100
X1 = 50
Y1 = 1
X2 = 20
Y2 = 91
X3 = 97
Y3 = 35
X4 = 2
Y4 = 35
X5 = 79
Y5 = 91
TEXT_X = 50
TEXT_Y = 35

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

        # Draw the star.
        self.canvas.create_polygon(X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5)

        # Write the name
        self.canvas.create_text(TEXT_X, TEXT_Y, text='Jasmine',
                                anchor= tkinter.N, fill='white')
        
        # Pack the canvas.
        self.canvas.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()