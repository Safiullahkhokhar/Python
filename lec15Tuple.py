# tupe is similar to the list but difference is that we cannot change the elements of a tuple once it is assigned

v1="hello"  #str
v2=("hello")    #tuple
print(v1,v2)

tp1 = ( ["Python", "Java"], (1, 2, 3) )
tp2 = ("C++","C#","C",40,50,60)
#print(type(tp)) # type is tuple
print(type(tp1),tp1)
print(tp1[0])
print(tp1[1])
print(tp2[0])
print(tp2[1])
print(tp2[2])
print(tp2[3])
print(tp2[4])
print(tp2[5])


#Access the element throuth slicing ":"
print(tp2[0:2])

# Negative indexing access
print(tp2[-2])
print(tp2[len(tp2)-2])
print(tp2[1])

# checking the element is present or not with the help of "in" keyword
if "C++" in tp2:
    print("C++ is avilable")
else:
    print("Not avilable") 

#Range index "Jump index"
print("Actul length: ",tp2)
print("0 to 4 length:",tp2[0:4])
print("0 to 4 jump 1:",tp2[0:4:1]) #last jump
print("0 to 4 jump 2:",tp2[0:4:2]) #1 jump
print("0 to 4 jump 3:",tp2[ :4:3]) #2 jump

#mainuplate tuples
#tuples are immutable, hance we can add,remove or change tuple items, than 1st you mus convert tuple to a list .Than perform operation on that list and convert it back to tuple

temp = list(tp2)
temp.append("added")    #add item
temp.pop(2)             #remove
temp[2]="Ruby"          #change
tp2 = tuple(temp)
print(tp2)

#method in tuple same as list
popvar= list(tp2)
popvar.pop(2)
print("Pop item:",popvar ,"Ruby index is [3]")
