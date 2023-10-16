# lecture1.txt file move outside the lec22FileModule than execute these programes
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

# with open("lecture1.txt",'a') as f:
#     f.write("hi I am safiullah...")


# creat a file 
# This mode creates a file and gives an error if the file already exists.


# readline()
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student of {i} in Maths is: {m1 * 2}")
#     print(f"Marks of student of {i} in English is: {m2 * 2}")
#     print(f"Marks of student of {i} in Cs is: {m3 * 2}")
#     print(line)

# writelines()
# Python writes a sequence of strings to a file. 
# The sequence can be any iterable object, such as a list or a tuple.

# f = open('myfile2.txt', 'w') # if file is not aviable than create a new file
# lines = ['line1\n','line2\n','line3\n','line4\n'] # in file print lines 1 to 4
# f.writelines(lines)
# f.close()

# If you want to add newlines between the strings, 
# you can use a loop to write each string separately

# f = open('myfile2.txt', 'w') # if file is not aviable than create a new file
# lines = ['line1\n','line2\n','line3\n','line4\n'] # in file print lines 1 to 4
# for line in lines:
#         f.write(line + '\n')
# f.close()