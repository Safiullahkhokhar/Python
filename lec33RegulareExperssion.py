# Regular Experssion re
#Regular expressions, or "regex" for short, are a powerful tool 
# for working with strings and text data in Python. They allow you
#  to match and manipulate strings based on patterns, making it easy 
#   to perform complex string operations with just a few lines of code.

import re

pattern = r"[A-Z]+atch" # raw str "r", [A-Z] All char: A to Z, "+" 1 or more occurrence/event, atch in last
text = """ 
The span() method in Python is used to get the start and end positions of a 
Matched regular expression. It is a method of the Match object, which 
is returned by the Match() and search() methods of the re module.
Catch Latch
"""

# either returns None (if the pattern doesn’t match), 
# or a re.MatchObject that contains information about the matching part of the string. 
# method stops after the first match, so this is best suited for testing 
# a regular expression more than extracting data. 
match = re.search(pattern, text)
print(match)
# output is <re.Match object; span=(79, 84), match='Match'>

# returns a list containing all matches.
matches = re.findall(pattern, text)
print(matches)
# OP is['Match', 'Match', 'Match', 'Catch', 'Latch']

# returns a new string with all occurrences of the pattern replaced with
#  the replacement string. If the pattern is not found in the input string,
#  the original string is returned.
replace_text = re.sub(pattern, "Hy", text)
print(replace_text)
# the output is :
# The span() method in Python is used to get the start and end positions of a 
# Hyed regular expression. It is a method of the Hy object, which 
# is returned by the Hy() and search() methods of the re module.
# Hy Hy

 

# # difference b/t string and raw string
# string = "This is a string with a newline character: \n"
# print(string)

# raw_string = r"This is a raw string with a backslash: \n"
# print(raw_string)
