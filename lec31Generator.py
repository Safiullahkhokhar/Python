# Generator 

# It's special type of functions that allow you to create an iterable sequence of values.
# It  returns a generator object, which can be used to generate the values one-by-one 
#  as you iterate over it. Generators are a powerful tool for working with large 
#   or complex data sets, as they allow you to generate the values on-the-fly, 
#    rather than having to create and store the entire sequence in memory.
# you can create a generator by using the yield statement in a function.
# yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. 

def my_gen():
    for i in range(5):
        yield i
gen = my_gen()
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #3

#my_generator() returns a generator object, which can be used to generate 
# the values in the range 0 to 4. 
# The next() function is used to request the next value from the generator,
#  and the generator resumes its execution until it reaches the end of the function.

# Benefit of generators is that they are lazy, which means that the values
#  are generated only when they are requested. This allows you to 
#  the values in a more efficient and memory-friendly manner, as you don't 
# have to generate all the values up front.

#Generators in Python are a powerful tool for working with large
#  or complex data sets, allowing you to generate the values on-the-fly
#  and store only what you need in memory. 
# Whether you are working with a large dataset, performing complex calculations,
#  or generating a sequence of values, generators are a must-have
#  tool in your programming toolkit. So, if you haven't already, 
# be sure to check out generators in Python and see how they can 
# help you write better, more efficient code.