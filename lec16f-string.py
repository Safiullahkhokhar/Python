# f-string 
# Introduced by the PEP 498
# Also known as Literal String Interpolation or 
# more commonly as F-strings (f character preceding the string literal).
# Focus of this mechanism is to make the interpolation easier  
# The letter 'f', the string becomes the f-string itself. 
# The f-string can be formatted in much same as the str.format() method.
# f-string offers a convenient way to embed Python expression inside string literals for formatting

name ="Safi"
age = 19
print(f"hy, I am {name} and I am {age} years old. ")

print(f"{2 * 30}")
