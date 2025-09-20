#QUIZ GAME

print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct Answer! :)")
    score += 1
else:
    print('Incorrect Answer! :(')

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("Correct Answer! :)")
    score += 1
else:
    print('Incorrect Answer! :(')

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct Answer! :)")
    score += 1
else:
    print('Incorrect Answer! :(')

# Question 4
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory" :
    print("Correct Answer! :)")
    score += 1
else:
    print('Incorrect Answer! :(')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
print("Thanks for playing!")
