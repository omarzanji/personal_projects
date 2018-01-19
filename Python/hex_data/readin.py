'''
This program will read in a csv file and grab hex data and store in numpy array as int.

Notes: 128 bit data is represented as 32 chars. You can compress the 128 bit data
       to 32 bit by only storing the first 8 chars of the 32 chars. Although this
       is a less accurate reading, it can still be used. This program does just that.

@author Omar Barazanji
@version 2018
'''

import numpy as np
import matplotlib.pyplot as pp
import Tkinter as tk
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

# Makes sure that whole numpy array gets printed
np.set_printoptions(threshold=np.nan)
np.set_printoptions(formatter={'float_kind':'{:f}'.format})


'''
This function will slice every string in a numpy array to a specified endpoint.
'''
def slice(a, end):
    # Populate new np array with values of old np array.
    b = np.array([])
    # For every string element in a, slice to endpoint and store in b.
    for x in a:
        val = x[:end]
        b = np.append(b, val)
    return b

'''
This function will convert string represented as hex to an int value and store in a new numpy array.
'''
def toHex(a):
    # Populate new np array with values of old np array.
    b = np.array([])
    # For every string element in a, convert to hex and store in b.
    for x in a:
        hex_val = int(x, 16)
        b = np.append(b, hex_val)
    return b

'''
This function will plot 1-D data in PyPlot graph.
'''
def plot1D(a):
    y = 0
    pp.plot(a, np.zeros_like(a) + y, 'x')
    pp.show()

'''
The code below will be a Tkinter interface for the tool.
'''
interface = tk.Tk()

def select_file():
    global filename
    filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                 filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    L2 = tk.Label(interface, text=str(filename))
    L2.grid(row=1, column=1)

def ok_command():
    global columnNum
    columnNum = int(E1.get()) - 1
    interface.destroy()
    print(columnNum)

L1 = tk.Label(interface, text="Select CSV File")
L1.grid(row=0, column=0)

B1 = tk.Button(interface, text="Browse", command=select_file)
B1.grid(row=0, column=1)

L3 = tk.Label(interface, text="Enter Column Number: ")
L3.grid(row=3, column=0)

E1 = Entry(interface, bd=5)
E1.grid(row=3, column=1)

B2 = tk.Button(interface, text="Plot", command=ok_command)
B2.grid(row=4, column=1)

interface.title('Hex Interpreter')
interface.mainloop()

# Read in CSV file and populate  array, TDATA (128bit data).
TDATA = np.loadtxt((str(filename)), dtype=str, delimiter=',', skiprows=1, usecols=(columnNum,))

# Slice each string in TDATA to its 32bit point (8 from start).
TDATA_sliced = slice(TDATA, 8)

# Convert string to hex value represented as int.
TDATA_sliced_toHex = toHex(TDATA_sliced)

# Prints TDATA hex data in int format
print(TDATA_sliced_toHex)

# Plot data
plot1D(TDATA_sliced_toHex)