# Dictionary is the collection that allows to store key values pairs

dic={
    'Safiullah':'Human being',
    'Spoon':'Object',
    'Tiger':'Animal'
}

# print all dic items
print(dic)

#the length of a dictionary is 3
print(len(dic))

#Access the value of a dictionary by placing the key in side {} brackets 
print(dic['Safiullah'])

print(dic.get("Khan"))# print none because their is not avilable in dictionary but it cannot through an error
#print(dic['Khan'])# it'll get through an error

# Also Acess the value of a dic
print(dic.get("Safiullah"))

# Valid dictionary
my_dict = {
    2112121: "Safiullah",
    2112124:"Sarfarz", 
    (1, 2): "Hello Hi", 
    3: [1, 2, 3]
}
print(my_dict)
print(my_dict[2112121])

# Invalid dictionary
# Error: using a list as a key is not allowed
# my_dict = {
#     1: "Hello", 
#     [1, 2]: "Hello Hi", 
# }
# print(my_dict)

print(dic.keys())# Access all the keys

print(dic.values())# Access all the values

#or
# access all the corsponding values 
for key in dic.keys():
    #print(dic[key])
    print(f"The value corsponding to the {key} is {dic[key]} ")

# access all the key value pairs using items keyword
print(dic.items())
#or
for key, value in dic.items():
    print(f"The value corsponding to the {key} is {value} ")

#Add item to a dic
dic['Pakistan'] = "Islamabad" 
print('Add new item:',dic)

#Change dic items
dic['Pakistan'] = "Karachi" 
print('Change item:',dic)

#Remove dic item
del dic['Pakistan'] 
print('Remove item',dic)

#methods 
print("Methods use in Dictionary")

#.update() updates the value of key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
dic.update({'Age':19})
print("Update items:",dic)

#.pop() Remove the key-value pair whose key is pass as a parameter
dic.pop('Tiger')
print("Pop items:",dic)

#.popitem() Remove the last key-value pair from the dictionary
dic.popitem()
print("Popitems :",dic)

#.values() access all the values
print("Values :",dic.values())

#.keys() access all the key
print("Keys :",dic.keys())

#.get() access item from dic
print("Get item :",dic.get("Safiullah"))

#.copy() Duplicate of a dictionary
print("Copy item :",dic.copy())

#.clear() Remove all the items
print("Clear items :",dic.clear())
