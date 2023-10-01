#Methods in Python

str= " Hello World !!! "
print(str.upper()) # All letters in capital
print(str.lower()) # All letters in small case
print(str.strip()) # Removes whitespaces before and after

str1="hello world !!!"
print(str1.rstrip("!")) # Removes any trailling char
print(str1.replace("h","l")) # Replace H to L
print(str1.split()) # Change into list
print(str1.capitalize()) # 1st char is upper and rest of lower
print(str1.center(50,".")) # String to the center as per user parameters
print(str1.count("l")) # Returns the number of time given value occurred
print(str1.endswith("!!!")) # Cheacks the string ends with a given value
print(str1.find("world")) # Search the 1st occurrence of the given value and return present index if the value is absent then return -1
print(str1.index("!!!")) # given value is absent then raise an exception

str2="helloworld"
print(str2.isalnum()) # Returns true only the consists of A-Z,a-z,0-9
print(str2.isalpha()) # Returns ture only the consists A-Z,a-z
print(str2.islower()) # Returns ture all the char in lower case
print(str2.isprintable()) # Returns true the given string is printable otherwise \n Flase
print(str2.isspace()) # Returns ture only the string contains whitespace,tab space otherwise False
print(str.istitle()) # Returns ture the 1st char of the string is capital
print(str2.isupper()) # Returns ture all the char of the string is capitalized
print(str2.startswith("hello")) # Return true string start with a given value
print(str2.swapcase()) # convert lower case to upper case and upper case to lower case
print(str2.title()) # capitalized the 1st char of the string 
