# snake water gun game
# Snake beats Water
# Water beats Gun
# Gun beats Snake
# If both players choose the same option, it is a draw.
import random
# random numbers select by comp
# print(random.randint(0 , 2))
# print(random.randint(0 , 2))

comp = (random.randint(0,2)) # computer random number
user = int(input("0 for Snake, 1 for Water and 2 for Gun: ")) # user take any num
# method for how mush chances that you were lose the game
def check(comp , user):
    if comp == user: # draw game 
        return 0
    if (comp == 0 and user ==1):
        return -1
    if (comp == 1 and user ==2):
        return -1
    if (comp == 2 and user ==0):
        return -1
    return 1 # otherwise you win

score = check(comp,user)

print("You:", user)
print("Computer:", comp) # which num computer select

if(score == 0):
    print("It's Draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")
    