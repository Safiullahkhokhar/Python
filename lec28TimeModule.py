# time module 
import time
# time.time()

def Whileloop():
    i=0
    while i< 3000:
        i += 1
        print(i)

def Forloop():
    for i in range(3000):
        print(i)
init = time.time()
Forloop()
t1 = time.time() - init

init = time.time()
Whileloop() # this id for Whileloop and its op is 2.41
print(time.time() - init)
print(t1)# this id for Forloop and its op is 1.25


# time.sleep
time.sleep(3) # sleep till 3 seconds complete than towards next statement
print("The time is printed after 3 sec")
print(time.time())

# strftime
t = time.localtime()
formated_time = time.strftime("%y-%m-%d %H:%M:%S")
print(formated_time)