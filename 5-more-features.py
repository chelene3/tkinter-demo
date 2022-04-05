from tkinter import Tk, Button, Entry, Label, filedialog
import tkinter.messagebox

obj = Tk()
obj.config(width=1000, height=500)

#Create Labels
title = Label(text="Define Parameters", font=("Arial", 25), justify="center")

position_label = Label(text="Position")
velocity_label = Label(text="Velocity")
acceleration_label = Label(text="Acceleration")
jerk_label = Label(text="Jerk")
time_label = Label(text="Time Scale")

#Create Entries
position_field = Entry()
velocity_field = Entry()
acceleration_field = Entry()
jerk_field = Entry()
time_field = Entry()

#Command for the button
#Create a pop-up window
def apply_click():
    tkinter.messagebox.showinfo("Alert")

#Create Apply Button
click_button = Button(text="Apply Changes", command=apply_click)

def browse_click():
    filename = filedialog.askopenfilename(initialdir='/Users/chelsearowe/Desktop/', title= "Select a Preset")
    print(filename)

#Create Browse Button
browse_button = Button(text="Browse Files", command=browse_click)
 
#Place all widgets 
title.grid(row=0, column=0, columnspan=3)
position_label.grid(row=1, column=0)
velocity_label.grid(row=2, column=0)
acceleration_label.grid(row=3, column=0)
jerk_label.grid(row=4, column=0)
time_label.grid(row=5, column=0)

position_field.grid(row=1, column=2)
velocity_field.grid(row=2, column=2)
acceleration_field.grid(row=3, column=2)
jerk_field.grid(row=4, column=2)
time_field.grid(row=5, column=2)

click_button.grid(row=6, column=0, columnspan=3)
browse_button.grid(row=7, column=0, columnspan=3)

obj.mainloop()