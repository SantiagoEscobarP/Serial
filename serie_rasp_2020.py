# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:08:08 2020

@author: edwar
"""
from tkinter import *
#from tkinter import ttk
import serial 


ser = serial.Serial('COM2')
root = Tk()
root.geometry("400x300")
setpoint = IntVar()

def sel():
   selection = "Value = " + str(setpoint.get())
   selection=selection.encode();
   ser.write (selection) 
   label.config(text = selection)
   print (str(setpoint.get()) + '\n')

#ser.write(b'hello')
#sio.write(unicode("hello\n"))

leer = Button(root, text = "leer barra", command = sel)
barra = Scale (root, variable = setpoint)
barra.place(x=200,y=100)
label = Label(root)


label.pack()
leer.pack(anchor = CENTER)
#barra.pack()
root.mainloop()