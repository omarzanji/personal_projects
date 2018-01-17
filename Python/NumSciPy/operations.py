'''
this program will run basic operations on a csv file.
@author Omar Barazanji
@version 2018
'''

import numpy as np

file_data = np.loadtxt("Book.csv", delimiter=",")
print(file_data)


# Below is an interaction with the user to run operations on the array "file"
choice = 'Y'
while choice in ['Y', 'y']:
    print('1 - Average, 2 - Add, 3 - Multiply')
    op_choice = raw_input('Select an operation: ')

    # Average method
    if op_choice in ['1', 'Average', '1 - Average']:
    	print('1 - Average a row, 2 - Average a column')
        choice_avg = raw_input('Select an Average operation: ')
        # Average row method
        if choice_avg in ['1', 'Average a row', '1 - Average a row']:
            rows = len(file_data) # num of rows
            i = 0
            while (i < rows):
                current_row = file_data[i]
                print('Row %d: ' % (i) + str(current_row))
                i += 1
            choice_row = input('Select a row to average: ')
            print(sum(file_data[choice_row])/len(current_row))   
        # Average column method
        if choice_avg in ['2', 'Average a column', '2 - Average a column']:
            columns = 1 + file_data.shape[0] # num of columns
            i = 0
            while (i < columns):
                current_column = file_data[:, i]
                print('Column %d: ' % (i) + str(current_column))
                i += 1
            choice_column = input('Select a column to Average: ')
            print(sum(file_data[:, choice_column])/len(current_column))

    # Add method
    if op_choice in ['2', 'Add', '2 - Add']:
        print('1 - Add a row, 2 - Add a column')
        choice_add = raw_input('Select an add operation: ')
        # Add row method
        if choice_add in ['1', 'Add a row', '1 - Add a row']:
            rows = len(file_data) # num of rows
            i = 0
            while (i < rows):
                current_row = file_data[i]
                print('Row %d: ' % (i) + str(current_row))
                i += 1
            choice_row = input('Select a row to add: ')
            print(sum(file_data[choice_row]))
        # Add column method
        if choice_add in ['2', 'Add a column', '2 - Add a column']:
            columns = 1 + file_data.shape[0] # num of columns
            i = 0
            while (i < columns):
                current_column = file_data[:, i]
                print('Column %d: ' % (i) + str(current_column))
                i += 1
            choice_column = input('Select a column to add: ')
            print(sum(file_data[:, choice_column]))

    # Multiply method
    if op_choice in ['3', 'Multiply', '2 - Multiply']:
        print('1 - Multiply a row, 2 - Multiply a column')
        choice_mult = raw_input('Select an Multiply operation: ')
        # Multiply row method
        if choice_mult in ['1', 'Multiply a row', '1 - Multiply a row']:
            rows = len(file_data) # num of rows
            i = 0
            while (i < rows):
                current_row = file_data[i]
                print('Row %d: ' % (i) + str(current_row))
                i += 1
            choice_row = input('Select a row to Multiply: ')
            print(np.prod(file_data[choice_row]))
        # Multiply column method
        if choice_mult in ['2', 'Multiply a column', '2 - Multiply a column']:
            columns = 1 + file_data.shape[0] # num of columns
            i = 0
            while (i < columns):
                current_column = file_data[:, i]
                print('Column %d: ' % (i) + str(current_column))
                i += 1
            choice_column = input('Select a column to Multiply: ')
            print(np.prod(file_data[:, choice_column]))

    choice = raw_input('Would you like to continue? Y for yes, N for no: ')
