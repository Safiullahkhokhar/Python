# Getter and Sette methods

# Getters are methods that are used to access the values
# of an object's properties. They are used to return the value of
#  a specific property, and are typically defined using the @property decorator. 

class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}") # 67.0
    
    @property # decorator

    # def value(self):
    #     return self._value

    # i will retrun the 10x time value
    # now this is getter 
    def ten_value(self):
        return 10* self._value 
    # cannot change the value of getter so applying setter method to change the value
    #setter
    @ten_value.setter
    def ten_value(self, new_value):
        self._value= new_value /10 # 1000/10 =100
       

obj= MyClass(10)
obj.show()# value is 10
print(obj._value)#10
obj.ten_value= 67 # cannot change the value if we'll chagne it, than apply the setter method
print(obj.ten_value) # 100


#It is important to note that the getters do not take any parameters and
#  we cannot set the value through getter method.For that we need setter
#   method which can be added by decorating method with @property_name.setter

# In conclusion, getters are a convenient way to access the values of an object's properties,
#  while keeping the internal representation of the property hidden. 
#   This can be useful for encapsulation and data validation.