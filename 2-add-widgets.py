from tkinter import Tk, Button, Entry, Label

obj = Tk()
obj.config(width=1000, height=500, bg="white")

#Create a button
click_button = Button(text="Click Me", command="")
click_button.pack()

#Add an entry field
text_field = Entry()
text_field.pack()

#Create a label
name = Label(text="Demo of a Label")
name.pack()


obj.mainloop()