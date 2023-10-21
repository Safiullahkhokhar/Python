# Inheritance
# Single 
class Parent:
    def fun1(self):
        print("This function is in Parent class")

class Child(Parent):
    def fun2(self):
        print("This function is in Child class")
obj1=Child()
obj1.fun1()
obj1.fun2()

# Multiple
class Father:
    fathername="Ali"
    def father(self):
        print(self.fathername)

class Mother:
    mothername= "Amna"
    def father(self):
        print(self.mothername)

class Son(Father,Mother):
    def parent(self):
        print(f"My father name is {self.fathername} and my mother name is {self.mothername}")
obj2=Son()
obj2.parent()
# By mistake if you change the name than
# obj2.fathername=" "
# obj2.mothername=" "

# Multilevel
class Grand_father:
    def __init__(self, grand_father_name):
        self.grand_father_name = grand_father_name 

class Father(Grand_father):
    def __init__(self,father_name,grand_father_name):
        self.father_name = father_name
        Grand_father.__init__(self, grand_father_name)
        
class Son(Father):
    def __init__(self, son_name,father_name, grand_father_name):
        self.son_name = son_name
        Father.__init__(self,father_name,grand_father_name)

    def print_names(self):
        print(f"My GrandFatherName is {self.grand_father_name} and my fatherName is {self.father_name} so my name is {self.son_name}")

obj3=Son("Ali Ahmed","Ahmed","Ali")
obj3.print_names()

# Hierarchical
class Parent:
    def fun_1(self):
        print("This function is in Parent class")

class Child1(Parent):
    def fun_2(self):
        print("This function is in Chile1 class")

class Child2(Parent):
    def fun_3(self):
        print("This function is in Child2 class")
obj4=Child1()
obj4.fun_1()
obj4.fun_2()
obj41=Child2()
obj41.fun_1()
obj41.fun_3()

# Hybrid
class School:
    def func1(self):
        print("This function is in school.")
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1,School):
    def fun_4(Student1,School):
        print("This function is in student 3.")
obj5=Student3()
obj5.func1()
obj5.func2()