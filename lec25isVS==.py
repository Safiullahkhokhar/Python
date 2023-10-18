# 'is' operation vs '==' operation
# Both comparison operators that can be used to check if two values are equal
# 'is' operator compares the identity of two objects
# '=='  operator compares the values of the objects
# 'is' will only return True if the objects being compared are the exact same object in memory
# '==' will return True if the objects have the same value.

a = 4
b = 4
print(a == b) # True value
print(a is b) # True exect location of object in memory


a= (1,2)
b= (1,2)
# print(a == b) # True value
# print(a is b) # True exect location of object in memory

a= None
print(a is None)# true

a=[1,2,3]
b=[1,2,3]
print(a is b)#false
print(a==b)# ture
