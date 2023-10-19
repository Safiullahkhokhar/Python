# oop in Python

# A class is a blueprint or a template for creating objects,
#  providing initial values for state (member variables or attributes), 
#   and implementations of behavior (member functions or methods). 
#     The user-defined objects are created using the class keyword.

# creating class
class Person:
    name ='safi'
    occupation = 'software developer'
    networth = 15
    #function
        #self parameter is a reference to the current instance of the class,
        #  and is used to access variables that belongs to the class.
    def info(self):
        print(f"{self.name} is a {self.occupation}")

# Object is the instance of the class used to access 
#  the properties of the class Now lets create an object of the class.
obj = Person()

print(obj.name,obj.occupation,obj.networth)# access Person class propreties

# change properties of a class 
obj.name = 'safiullah' 
obj.occupation= 'Software engineer'
obj.networth= '20'
print(obj.name,obj.occupation,obj.networth)
obj.info()

obj.name = 'Khan' 
obj.occupation= 'QA Tester'
obj.networth= '25'
print(obj.name,obj.occupation,obj.networth)
obj.info()

ob= Person()
ob.name = 'Khan Shan' 
ob.occupation= 'FeedBack'
ob.networth= '10'
print(ob.name,ob.occupation,ob.networth)
ob.info()