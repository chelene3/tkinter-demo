from tkinter import Tk

# Create object and configure the width and height 
obj = Tk()
obj.config(width=1000, height=500)

# This line runs the tkinter event loop listening for button clicks, key presses, etc
# Blocks the code after it from running until the window is closed 
# Usually the last line of the file
obj.mainloop()