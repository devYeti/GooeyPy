# First project to implement a GUI
# Working along with the Programming Hero app
# David Wakeley github.com/devYeti 

from tkinter import *
from PIL import ImageTk, Image

# create app window
root = Tk()  # Create Tk() class object 
root.title('Ooohy Gooey!') # Title for root window
root.geometry('500x200') # define window size 

# Create widget objects: 
course = Label(root, text = 'Programming Hero Course', bg = 'red', fg = 'white')
enroll = Button(root, text = 'Enroll Now',fg = 'blue', bg = 'yellow')
lbl = Label(root, text = 'Name')
data = Entry(root)

# open image and create object:
img_lbl = Label(root, text = 'Python')
img = Image.open('python_logo.png')
picture = ImageTk.PhotoImage(img)
python = Label(root, image = picture)

# Place widgets in root window:
img_lbl.grid(row = 0, column = 2)
python.grid(row = 1, column = 2)
course.grid(row = 2, column = 1)
enroll.grid(row = 3, column = 1)
lbl.grid(row = 4, column = 0)
data.grid(row = 4, column = 1)

root.mainloop()
