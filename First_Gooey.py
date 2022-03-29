# First project to implement a GUI
# This project doesn't actually do anything
# It's just for practice and learning
# Working along with the Programming Hero app
# David Wakeley github.com/devYeti 

import tkinter.font as font
from tkinter import *
from PIL import ImageTk, Image

# enroll event function
def enroll():
    output['text'] = 'Enrolled Successfully'

# create app window
root = Tk()  # Create Tk() class object 
root.title('Ooohy Gooey!') # Title for root window
root.geometry('600x700') # define window size 

# font tuple:
font = font.Font(family = 'Serif', size = 18, weight = 'bold')

# Create widget objects: 
course = Label(root, text = 'Programming Hero Course', bg = 'red', fg = 'white', font = font)
enroll = Button(root, text = 'Enroll Now',fg = 'blue', bg = 'yellow', command = enroll)
lbl = Label(root, text = 'Name')
data = Entry(root)
output = Label()

# open image and create object:
img_lbl = Label(root, text = 'Python')
img = Image.open('python_logo.png')
picture = ImageTk.PhotoImage(img)
python = Label(root, image = picture)

# Place widgets in root window:
img_lbl.grid(row = 0, column = 2)
python.grid(row = 1, column = 2)
course.grid(row = 2, column = 2)
lbl.grid(row = 3, column = 1)
data.grid(row = 3, column = 2)
enroll.grid(row = 4, column = 2)
output.grid(row = 5, column = 2)

root.mainloop()
