# Enumerate Function is a built-in function
# Python allows you to loop over a sequence (such as a list, tuple, or string)
#  and get the index and value of each element in the sequence at the same time.
# Without enumerator function
marks1 = [10,20,30,90,50]
index1 = 0
for mark1 in marks1:
    print(mark1)
    if index1 == 3:
        print("Good work!")
    index1 +=1

# With enumerate function
marks = [10,20,30,90,50]
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("good work safi ")

# By default, the enumerate function starts the index at 0, 
# but you can specify a different starting index by passing it as an argument

names = ['Safiullah','Attiullah','Hasseb']
for index2, name in enumerate(names, start=1):
    print(index2,name)
#OR

for index2, name in enumerate(names):
 print(f"{index2 + 1}: {name}")

 # Loop over a string and print the index and value of each character
s = 'safiullah'
for index, c in enumerate(s):
    print(index, c)