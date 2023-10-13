# Coding to Decoding exercise

# Python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

ip = input("Enter message: ")
words= ip.split(" ") # seperated string 
coding= input("Press 1 for code and 0 for decode: ")
coding= True if(coding == "1") else False # 1 than coding 
print(coding) # Ture or False 

if(coding):
    nwords= [] # new words append to it
    for word in words:
        if(len(word)>=3): #atleast 3 characters
            r1= "ras"
            r2="jyh"
            stnew= r1+ word[1:] + word[0] + r2 #three random characters at the starting and the end
            nwords.append(stnew) #now append
        else: # <=3
            nwords.append(word[::-1]) # reverse 
    print(" ".join(nwords)) # elements will be joined
else: # decoding
    nwords= [] # new words append to it
    for word in words:
        if(len(word)>=3): #atleast 3 characters
            stnew= word[3 : -3] # remove three random characters at the starting and the ending
            stnew= stnew[-1] + stnew[:-1] # last char to the fist
            nwords.append(stnew) #now append
        else: # <=3
            nwords.append(word[::-1]) # reverse 
    print(" ".join(nwords)) # elements will be joined