# Guess the Number

# ye program ek random number generate krke dega, jisko hum ek varible me store kra lenge (lets say target variable)
# fir ham user se baar baar number input lenge (lets say it user's choice)
# if choice == target -----> give congratulations
# if choice < target ---> give num is less than target
# if choice > target ---> give num is greater than target
# By using Loops


# For this project we have to import a module called random , which generates a random number within a range

import random            # to generate random value

target = random.randint(1, 100)   # End point included   # generated value stored in target variable
# randint(1, 100)  -> generate random integer between 1 to 100

while True:       # True , taki jo bhi number choose kre usko loop me accept krle
    choice = input("Enter your choice or Quite(Q): ")

    if(choice == "Q"):
        break       # Agar Q dala tp yahi par exit ho jayega

    choice = int(choice)    # typecasting the choice from string to int
    if(choice == target):
        print("Congrates! You got it right..")
        break

    elif(choice < target):
        print("Youe number is samll, Enter a bigger choice..")

    else:
        print("Your number is big, Enter a smaller choice..")

print("GAME OVER !")