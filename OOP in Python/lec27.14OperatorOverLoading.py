# Operator OverLoading

# You can overload an operator in Python by defining special
#  methods in your class. These methods are identified by their names,
#   which start and end with double underscores (__). Here are some of the most 
#    commonly overloaded operators and their corresponding special methods:
class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))

# It's important to note that operator overloading is not 
#  limited to the built-in operators, you can overload any user-defined operator as well.


# Operator overloading is a powerful feature in Python that
#  allows you to create more readable and intuitive code. 
#   By redefining the behavior of mathematical and comparison
#    operators for custom data types, you can write code that is both
#      concise and expressive. However, it's important to use operator 
#       overloading wisely, as overloading the wrong operator or using it
#         inappropriately can lead to confusing or unexpected behavior.
    