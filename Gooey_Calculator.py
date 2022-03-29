# Project to create a basic calculator with GUI
# David Wakeley github.com/devYeti

from tkinter import *
import tkinter.font as font

root = Tk()
num1 = Label(root, text = 'Enter first number:', font = ('Serif', 12))
enter1 = Entry(root)
num2 = Label(root, text = 'Enter second number:', font = ('Serif', 12))
enter2 = Entry(root)
