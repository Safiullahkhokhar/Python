# if __name__=="__main__" it is a built-in variable
# this file import to the main file 

def welcome():
    print("You are welcom from safi")
    print(__name__) #main
    
if __name__== "__main__":
    welcome()

def add2num(a,b):
    sum= a+b
    print(sum)

if __name__== "__main__":
  add2num(2,3)
