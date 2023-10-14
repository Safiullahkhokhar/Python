1# lecture1.txt file move outside the lec22FileModule than execute these programes
# file input and output
# read only file
# Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. 
# This mode opens the file for reading only and gives an error if the file does not exist.
# This is the default mode if no mode is passed as a parameter.

# f = open("lecacture1.txt",'r')
# text=f.read()
# print(text)
# f.close()


# write a file
#This mode opens the file for writing only and creates a new file if the file does not exist.

# f = open("lecacture1.txt",'w') 
# f.write("hi I am safi")
# f.close()

# appending a file
# This mode opens the file for appending only and creates a new file if the file does not exist

# f = open("lecacture1.txt",'a') 
# f.write("hi I am safiullah")
# f.close()

#keyword
# you can use the 'with' statement to automatically close the file after you are done with it

with open("lecacture1.txt",'a') as f:
    f.write("hi I am safiullah...")


# creat a file 
# This mode creates a file and gives an error if the file already exists.


