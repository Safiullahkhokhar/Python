#set is a collection of unique data and elements of set cannot be and duplicate 

student_id={2112121,21,23,25}
print(student_id)

mixedset={'safiullah',2112121,}
print(mixedset)

empty_dict={}
print('Type of empty_dict is:',type(empty_dict))

empty_set= set()
print('Type of empty_set is:',type(empty_set))

#cannot contain duplicate items
set1={2,3,4,2} # the output is {2,3,4}
print("Can't contain duplicate:",set1)

# Add item in a set 
student_id.add(21124)
print("Add new item: ",student_id)

# Update a set
mixedset.update(set1) #  update the set with items other collection types
print("Update itme:",mixedset)

#Remove item
mixedset.discard("safiullah")
print("Remove item: ",mixedset)
print("length of a set:",len(mixedset))


#Oprations and some methods 

# union of 2 sets
a={1,3,5,7,9}
b={2,4,6,8,1}

#perform union operation using | symbol
print("union using |:", a|b) 

#OR with union() method
print("union method:",a.union(b))

# intersection

#perform intersection operation using & symbol
print("intersection using &:", a&b) 

#OR with intersection() method
print("intersection method:",a.intersection(b))


#Difference b/w 2 sets

#perform Difference operation using - symbol
print("Difference using |:", a-b) 

#OR with difference() method
print("Difference method:",a.difference(b))

#Symmetric difference

#perform Symmetric difference operation using ^ symbol
print("Symmetric difference using |:", a^b) 

#OR with Symmetric_difference() method
print("Symmetric difference method:",a.symmetric_difference(b))
