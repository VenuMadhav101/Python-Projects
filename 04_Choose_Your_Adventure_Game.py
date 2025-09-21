#CHOOSE YOUR OWN ADVENTURE GAME

name = input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (left/right) ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? (walk/swim) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and kill you. You lose.")
        else:
            print("Not a valid option. You lose.")    

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)
