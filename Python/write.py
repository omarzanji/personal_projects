# This file will demonstrate writing to a new file through user input.	  #
# @name Omar Barazanji							  #
# @version 2018								  #
###########################################################################
import os

print('Welcome to the Comma Delimited File Writer')
filename = raw_input('Enter a file name: ')
f = open(filename, "w")
yes_no = "Y"
while(yes_no == "Y"):
	data = raw_input('Enter comma delimited data: ')
	f.write(str(data)+"\n")
	yes_no = raw_input('Would you like to continue adding to this file? Enter Y for yes, N for no: ')
	if yes_no == "N":
		f.close()
file_path = os.getcwd()
print('File saved to: '+file_path)

