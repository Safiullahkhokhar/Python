 # Lambda function in python
#Lambda function is a small anonymos function without a name.
# It's defined using the lambda keyword.
# syntex lambda arguments : experssion

double = lambda x: x*2
print(double(5))

cube= lambda x: x*x*x
avg = lambda x,y: (x + y)/2
print(avg(3,1))
print(cube(2))

# can we call a function into fuction ?
# the answer is yes so how ,
def appl(fx,value):
    return 6+ fx(value)
# print(appl(cube, 2))
print(appl(lambda x: x*x*x , 2))