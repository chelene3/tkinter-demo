from tkinter import Tk, Button, Entry, Label

obj = Tk()
obj.config(width=1000, height=500, bg="white")

#Create a button
click_button = Button(text="Click Me", command="")

#Add an entry field
text_field = Entry()

#Create a label
name = Label(text="Demo of a Label")

#Uncomment different organization decisions
#PACK - organizes widgets before placing them in the frame
"""
click_button.pack()
text_field.pack()
name.pack()
"""

#GRID - like a table, indicate which row and column to place the widget 
"""
click_button.grid(row=0, column=0)
text_field.grid(row=1, column=1)
name.grid(row=2, column=2)
"""

#PLACE - specify the x and y coordinates of the widget 
"""
click_button.place(height=50, width=100, x=200, y=30)
text_field.place(height=100, width=300, x=500, y=300)
name.place(height=100, width=200, x=0, y=200)
"""

obj.mainloop()