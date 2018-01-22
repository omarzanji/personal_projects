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
import matplotlib
matplotlib.use("wx")
from pylab import *
import Tkinter as tk
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox

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
This function will find the column number containing 128bit data.
'''
def find_column_num(filename):
    ALL_DATA = np.loadtxt((str(filename)), dtype=str, delimiter=',')
    # if no column found, function returns -1
    column = -1
    target = 32
    # Sets rows equal to number or rows in ALL_DATA
    rows = ALL_DATA.shape[0]
    # Sets cols equal to number of columns in ALL_DATA
    cols = ALL_DATA.shape[1]
    # x iterates from zero to rows
    for x in range(0, rows):
        # y iterates from zero to cols
        for y in range(0, cols):
            # if length of element in ALL_DATA = 32 (target)
            if len(ALL_DATA[x, y]) == target:
                # column is set equal to current column (column has been found!)
                column = y
                break
    return column
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

file_selected = -1
def select_file():
    global filename
    filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                 filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    global file_selected
    file_selected = 1
    L2 = tk.Label(interface, text=str(filename))
    L2.grid(row=2, column=2)
    global columnNum
    columnNum = find_column_num(filename)
    if columnNum > 0:
        actual_column = columnNum + 1
        L3 = tk.Label(interface, text='Located 128bit data! Using column %d for plotting.' % actual_column)
        L3.grid(row=3)
    else:
        tkMessageBox.showinfo("Error", "Unable to locate 128bit data in %s" % str(filename))

def ok_command():
    if file_selected > 0:
        interface.destroy()
    else:
        tkMessageBox.showinfo("Error", "No file selected")

def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        exit()

L1 = tk.Label(interface, text="Select CSV File")
L1.grid(row=1, column=0)

B1 = tk.Button(interface, text="Browse", command=select_file)
B1.grid(row=1, column=2)

B2 = tk.Button(interface, text="Plot", command=ok_command)
B2.grid(row=3, column=2)

interface.title('Hex Interpreter')
interface.protocol("WM_DELETE_WINDOW", on_closing)
interface.mainloop()

# Read in CSV file and populate  array, TDATA (128bit data).
TDATA = np.loadtxt((str(filename)), dtype=str, delimiter=',', skiprows=1, usecols=(columnNum,))

# Slice each string in TDATA to its 32bit point (8 from start).
TDATA_sliced = slice(TDATA, 8)

# Convert string to hex value represented as int.
TDATA_sliced_toHex = toHex(TDATA_sliced)

# Prints TDATA hex data in int format
print(TDATA_sliced_toHex)

interface2 = tk.Tk()
interface2.title("32bit to Decimal List")

scrollbar = Scrollbar(interface2)
scrollbar.pack(side=RIGHT, fill=Y)

list = Listbox(interface2, height=50, width=50)
i = 1
for x in np.nditer(TDATA_sliced_toHex):
    list.insert(i, str(x))
    i = i + 1
list.pack()

# attach listbox to scrollbar
list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)


# Plot data
thismanager = get_current_fig_manager()
thismanager.window.wm_geometry("+600+100")
plot1D(TDATA_sliced_toHex)

interface2.mainloop()
