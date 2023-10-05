#list in python
lis1=["Python","Java","C++",True, 5]
print(lis1)
#print(type(list1))
print(lis1[0])
print(lis1[1])
#print(lis1[2])

#Access the element throuth slicing ":"
print(lis1[0:2])

# Negative indexing access
print(lis1[-2])
print(lis1[len(lis1)-2])
print(lis1[1])

# checking the element is present or not with the help of "in" keyword
if "C++" in lis1:
    print("C++ is avilable")
else:
    print("Not avilable") 

#Range index "Jump index"
print("Actul length: ",lis1)
print("0 to 4 length:",lis1[0:4])
print("0 to 4 jump 1:",lis1[0:4:1]) #last jump
print("0 to 4 jump 2:",lis1[0:4:2]) #1 jump
print("0 to 4 jump 3:",lis1[ :4:3]) #2 jump

#List comprehension
ls1 = [i * i for i in range(10)]
print(ls1) 
ls1 = [i * i for i in range(10) if i %2 ==0] # even numbers from the ls1
print(ls1)
print(ls1[len(ls1)-3])
