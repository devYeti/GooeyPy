# Project to create a basic calculator with GUI
# David Wakeley github.com/devYeti

from tkinter import *
import tkinter.font as font

# Number Entry with labels
root = Tk()
num1 = Label(root, text = 'Enter first number:', font = ('Serif', 12))
enter1 = Entry(root)
num2 = Label(root, text = 'Enter second number:', font = ('Serif', 12))
enter2 = Entry(root)

# operator buttons:
add = Button(root, text = 'Add', width = 10, command = add)
sub = Button(root, text = 'Sub', width = 10, command = sub)
mul = Button(root, text = 'Mul', width = 10, command = mul)
div = Button(root, text = 'Div', width = 10, command = div)


# Grid locations:
num1.grid(row = 0, column = 0)
enter1.grid(row = 0, column = 1)
num2.grid(row =1, column = 0)
enter2.grid(row = 1, column = 1)
