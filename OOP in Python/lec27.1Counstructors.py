# constructor is a special method in a class 
#  used to create and initialize an object of a class. 
#   It's invoked automatically when an object of a class is created
# The main purpose of a constructor is to initialize or assign values 
#   to the data members of that class. It cannot return any value other than None

# class a constructure
# class Person:
#     def __init__(self):
#         print("hello i am constructure")

# a= Person()
# b= Person()
# self is automatically pass an argument
class Person1:
    # parameterized consturctor 
    def __init__(self, n , o):
        print("Hello this is consturctor")
        self.n = n # ali ,safiullah
        self.o = o # software developer, QA Tester

    def info (self):
        print(f"{self.n} is a {self.o}")

d= Person1('ali', 'software developer')
d.info()

c= Person1( 'safiullah', 'QA Tester')
c.info()


class a:
    def __init__(self) -> None:
        print("This is Default Constructor")
e = a()
