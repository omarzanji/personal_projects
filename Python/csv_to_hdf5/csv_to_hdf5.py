'''
This program will convert a CSV to HDF5.

@author Omar Barazanji
@version 2018
'''

import numpy as np
import h5py
import Tkinter as tk
import tkFileDialog
from Tkinter import *


# Puts inputted file into a numpy array for h5py to use
def to_array(file_path):
    file_array = np.loadtxt(str(file_path), dtype=str, delimiter=',')
    return file_array


# Prompts the user to select a file and stores the dir for later use
def select_file():
    global filepath
    filepath = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                            filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    # If a file was selected, add B2 (Convert) button
    if len(str(filepath)) > 0:
        L3 = tk.Label(interface, text=str(filepath))
        L3.grid(row=5, column=1)
        B2.grid(row=6, column=1)


# Converts the file's numpy array into an hdf5 and stores it in the same dir as program (for now)
def convert_button():
    file_array = to_array(filepath)
    h5_file_name = "%s.h5" % find_filename(filepath)
    hdf5 = h5py.File(h5_file_name, 'w')
    hdf5.create_dataset('dataset_1', data=file_array)
    hdf5.close()
    L4 = tk.Label(interface, text="Done! File saved as %s.h5 in the same directory as this program."
                                  % find_filename(filepath))
    L4.grid(row=7, column=1)


# Parses through a dir string and returns the .csv filepath
def find_filename(path):
    # Removes the .csv extension from the file path
    no_csv = path[:-4]
    global slash_index
    i = -1
    while True:
        element = no_csv[i]
        if element == "/":
            slash_index = i + 1
            break
        i -= 1
    return no_csv[slash_index:]


# Defines a Tkinter GUI for the program to use
interface = tk.Tk()
# Label 1
L1 = Label(interface, text="Welcome to CSV to HDF5", font="Helvetica 18 bold")
L1.grid(row=0, column=1, padx=40)
# Label 2
L2 = tk.Label(interface, text="Select a CSV file to Convert")
L2.grid(row=2, column=1, padx=20)
# Button 1
B1 = tk.Button(interface, text="Browse", command=select_file)
B1.grid(row=3, column=1, padx=20)
# Button 2 (initialized when file is selected -- see selected_file method above)
B2 = tk.Button(interface, text="Convert", command=convert_button)
# Label 4 (initialized when conversion is complete -- see find_filename method above)


# Adds an empty row at 1
interface.grid_rowconfigure(1, minsize=20)
# Adds an empty row at 4
interface.grid_rowconfigure(4, minsize=15)

# Starts the GUI
interface.mainloop()
