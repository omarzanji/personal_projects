'''
This program will demonstrate the basics of using h5py with numpy.

Concepts explored: writing a new hdf5 file with numpy arrays, reading in an hdf5 file
                   creating datasets, creating groups, creating subgroups

@author Omar Barazanji (with the help of Noureddin Sadawi - YouTube)
@version 2018
'''

import numpy as np
import h5py

matrix1 = np.random.random(size = (1000, 1000))
matrix2 = np.random.random(size = (1000, 1000))
matrix3 = np.random.random(size = (1000, 1000))
matrix4 = np.random.random(size = (1000, 1000))


# The below statement sets the h5py file as object hdf (in write mode)
# This also ensures that the file is closed outside of the "with" block statement
with h5py.File('data.h5', 'w') as hdf:
    # Creates a dataset populated by matrix1
    hdf.create_dataset('dataset1', data=matrix1)
    # Creates a dataset populated by matrix 2
    hdf.create_dataset('dataset2', data=matrix2)

# The below statement sets the h5py file as an object hdf (now in read mode)
with h5py.File('data.h5', 'r') as hdf:
    # The below function shows all the datasets (keys) in the hdf5 file
    ls = list(hdf.keys())
    print('List of datasets in this file: \n', ls)
    # This assigns "data" to the properties of dataset1
    data = hdf.get('dataset1')
    print(data)
    # dataset1 should now be the same as matrix1
    dataset1 = np.array(data)
    print('Shape of dataset1: \n', dataset1.shape)
    print('dataset1: \n', dataset1)

###########################################################################
# Alternative way of dealing with files (as opposed to using "with" block:
f = h5py.File('data.h5', 'r')
ls = list(f.keys())
# Now you have to close the file when finished...
f.close()
###########################################################################

# Creating groups:
with h5py.File('data.h5', 'w') as hdf:
    # Sets G1 equal to a new group called "Group1"
    G1 = hdf.create_group('Group1')
    # Creates a dataset inside "Group1" populated by matrix1
    G1.create_dataset('dataset1', data=matrix1)
    # Creates a dataset inside "Group1" populated by matrix4
    G1.create_dataset('dataset4', data=matrix4)

    # Sets G2 equal to a new group's ("Group2") subgroup called "SubGroup1"
    G2 = hdf.create_group('Group2/SubGroup1')
    # Creates a dataset inside "SubGroup1" populated by matrix3
    G2.create_dataset('dataset3', data=matrix3)

    # Sets G3 equal to Group2's subgroup called "SubGroup2"
    G3 = hdf.create_group('Group2/SubGroup2')
    # Creates a dataset inside "SubGroup2" populated by matrix2
    G3.create_dataset('dataset2', data=matrix2)

