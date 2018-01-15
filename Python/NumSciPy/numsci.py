print("                                                                  ")
print("##################################################################")
print("##################################################################")
print("###                  - NUMPY AND SCIPY DEMO -                  ###")
print("##################################################################")
print("##################################################################")

import numpy as np

x = 5
x_squared = x**2
x_cubed = x**3
print("%d squared is %d" % (x, x_squared))
print("%d cubed is %d" % (x, x_cubed))

theta = 45
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)
print("if theta = %d, then sin(theta) = %d" % (theta, sin_theta))
print("if theta = %d, then cos(theta) = %d" % (theta, cos_theta))


# To create a row vector, use np.linespace function with the params:
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# meaning: start : scalar
#               The starting value of the sequence.
#          stop : scalar
#               The end value of the sequence, unless endpoint is set to False.
#               In that case, the sequence consists of all but the last of 
#               num + 1 evenly spaced samples, so that stop is excluded. 
#               Note that the step size changes when endpoint is False.
#
#          num : int, optional
#               Number of samples to generate. Default is 50. 
#               Must be non-negative.
#
#          endpoint : bool, optional
#               If True, stop is the last sample. Otherwise, it is not included.
#               Default is True.
#
#          retstep : bool, optional
#
#               If True, return (samples, step), where step is the spacing
#               between samples.
#
#          dtype : dtype, optional
#
#               The type of the output array. If dtype is not given, 
#               infer the data type from the other input arguments.

row_vector = np.linspace(-1.0, 1.0, num=20)
print(row_vector)

# To read in a csv file as an aray, use numpy.loadtxt
file_data = np.loadtxt("Book.csv", delimiter=",")
print(file_data)


# Below is an interaction with the user to run operations on the array "file"
choice = 'Y'
while (choice == 'Y'):
    print('1 - Average, 2 - Add, 3 - Multiply, 4 - Delete')
    choice = raw_input('Select an operation: ')
    if choice == '2' or choice == 'Add' or choice == '2 - Add':
        print('1 - Add a row, 2 - Add a column, 3 - Add selected values')
        choice_add = raw_input('Select an add operation: ')
        if choice_add == '1' or 'Add a row' or '1 - Add a row':
            # Add row method
            rows = len(file_data) # num of rows
            i = 0
            while i < rows-1:
                current_row = file_data[i]
                print('Row %d: ' % (i) + str(current_row))
                i += 1
            choice_row = input('Select a row to add: ')
            print(sum(file_data[choice_row]))
    choice = raw_input('Would you like to continue? Y for yes, N for no: ')
    
print("##################################################################")
print("##################################################################")
print("###                          - END -                           ###")
print("##################################################################")
print("##################################################################")
print("                                                                  ")
