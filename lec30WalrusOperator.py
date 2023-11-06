# walrus opetator
a= True
print(a:= False) # False

num = [1,2,3,4,5]
while (n := len(num)) > 0:
    print(num.pop())

# without walrus operator
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

# with walrus operator
foods = list()
while ( food := input ( "What food do you like?" )) != "quit":
    foods.append( food)