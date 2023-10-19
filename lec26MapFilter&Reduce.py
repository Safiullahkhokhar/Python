# Map Filter and Reduce function
# These are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. 
#These functions are known as higher-order functions, as they take other functions as arguments.

#Map
# A function to each element in a sequence and returns a new sequence containing the transformed elements.
# Function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
cube=lambda x: x*x*x
list1=[1,3,2,4,5,6,7,8,9]
# if we have a list so how can u find the cude
# using for loop 
# newl=[]
# for items in list1:
#     newl.append(cude(items))
# print(newl)

# using map function
#newl= map(cube,list1) map object return
newl= list(map(cube,list1))
print(newl)

# Filter
# Filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

filter1= lambda x: x>3
new2 = list(filter(filter1,list1))
print(new2)


# Reduce
#  It is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python
#  Function Argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.
# It  applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. 
# The reduce function returns the final result.

from functools import reduce
# sum of 2 numbers
# sum = reduce(lambda x, y: x + y, list1)
sum= lambda a,b : a+b
print(reduce(sum,list1)) 