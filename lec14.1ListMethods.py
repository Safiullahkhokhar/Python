#List Methods 

l = [1,3,2,6,4,7,9,8,5]
print("the list is:",l)

l.append(10) # append to add an item to the end of the list
print("Append:",l)

l.sort()    #Sort the list in acending order
print("Sort in ascending: ",l) 

l.sort(reverse=True)    #Sort and reverce the list in decending order
print("Sort in decending:",l)

l.insert(10,11) #insert an item on the specific index "10 is index"
print("Add new item: ",l)

l.remove(10)
print("Remove the item:",l) #remove item present at the given index "10"

l1=["Python","C#","C++","Java"]

l.extend(l1)    # add all item of an "l1"2nd list to the end of "l" 1st list 
print("Extend/merge 2 list:",l)

l.remove(9)    # remove the present item at the given index
print("Remove an item: ",l)

coptls= l.copy() #return shallow copy of the list
print("Copy list: ",coptls)

countvar=l1.count("C#") #return the count of specified item in the list
print("Count item:",countvar, "....index[1] of l2")

l1.reverse() #reverse the item of the list
print("Reverse item:",l1)

returnind=l1.index("C++")  #return the index of the 1st match item
print("Index return:",returnind ,"C++ index is [1]")

popvar=l1.pop(3)
print("Pop item:",popvar ,"python index is [3]")

l.clear()   #clear the item from the list
print("Clear the list:",l)