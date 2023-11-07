# Funcation Cashing
from functools import lru_cache
import time
@lru_cache(maxsize= None)

def fx(n):
    time.sleep(3)
    return n*3

print(fx(10))
print("Done for 10")
print(fx(20))
print("Done for 20")

print(fx(10))
print("Done for 10")
print(fx(30))
print("Done for 30")

#Function caching is a technique for improving the performance 
# of a program by storing the results of a function so that you 
# can reuse the results instead of recomputing them every time
#  the function is called. 
# In Python 3, function caching can be achieved using 
# the functools.lru_cache decorator, which provides an easy and
#  efficient way to cache the results of a function. 
# Whether you're writing a computationally expensive program, 
# or just want to simplify your code, function caching is a great
#  technique to have in your toolbox.

#Benefit of function caching is that it can simplify the code
#  of a program by removing the need to manually cache the 
# results of a function.
#  With the functools.lru_cache decorator, the caching is
#  handled automatically, so you can focus on writing 
# the core logic of your program.
