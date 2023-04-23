import random

def game(comp, b):
    if comp == b:
        return None
    elif comp == 's':
        if b == 'w':
            return False
        else:
            return True
    elif comp == 'w':
        if b == 'g':
            return False
        else:
            return True
    elif comp == 'g':
        if b == 's':
            return False
        else:
            return True


print("Comp has choosen his option")
randNo = random.randint(1,3)
# print(randNo)
if randNo == 1:
    comp = 's'
if randNo == 2:
    comp = 'w'
if randNo == 3:
    comp = 'g'
# print("computer choosed: ", comp)

b = input("Your turn: snake(s) water(w) gun(g):\n")

a = game(comp, b)

if a == None:
    print("The Game is Tie")
elif a:
    print("YOU win")
else:
    print("You LOSE")

print("computer choosed: ", comp)

