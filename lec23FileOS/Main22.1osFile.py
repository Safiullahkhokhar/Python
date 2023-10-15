# seek() and tell () function
# These function are used to work with file objects and their posotions within a file
# These functions a part of built-in io module,which provides a consistent interface for
#       reading and writing to various file like object,such as pips and in memory buffers. 

# seek() and tell () function
#  It allows you to move current position within a file to a specific point.
# The position is specified in bytes, and you can move either forword or backward from the current position

f= open('myfile2.txt','r')
f.seek(16) # move to the 16 byte to the file
print(f.tell())# return the current postion within the file in bytes => 16 
data = f.read(9) # read next 9 bytes
print(data)

#truncate () function
# if you want to truncate a file to a specific size,you can use the turncate fun
with open('trunfile.txt','w') as f:
    f.write("hello world")
    f.truncate(11)# hello world 

