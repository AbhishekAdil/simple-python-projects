# Snake ladder game 
# Module / libraries used - (1) random,  (2) time 
'''
# time module
import time
print("Hello world!")
time.sleep(3)         # Delay execution for a given number of seconds.
print("This is print after 3 seconds")
time.sleep(3)
print("print after 3 seconds")
'''

import random
import time

# Step 1.
# make dictionaries for snake and ladder values

snakes = {99 : 4,         #{start : end}
         70 : 54,         #{high -> low}
         52 : 40,
         24 : 10
         }

ladders = {6 : 25,        #{low -> high}
           11 : 45,
           60 : 84,
           46 : 90
           } 

# step 2.
# define a dice and its function

def roll_dice():
    return random.randint(1, 6)   # 6 is included

# step 3.
# define how player moves

def move_player(current_position, roll):
    print("You rolled a ", roll, "!")
    time.sleep(2)
    current_position += roll

# step 4.
# define conditions for all the posibility in the game
# 1st -> snake byte ( drop - kon se position se kitne number par drop hoga)
# 2nd -> ladders (up - kon se point se litna upar jayenge)
# 3rd -> else(no snake, no ladder), simply print the current position

    if current_position in snakes:
        print("Oh no! It's a snake bite! Go back from", current_position, "to", snakes[current_position])
        current_position = snakes[current_position]
        print("Your current position is ", current_position)

    elif current_position in ladders:
        print("Yay! Climed a ladder from", current_position, "to", ladders[current_position])
        current_position = ladders[current_position]
        print("Your current position is ", current_position)

    else:
        print("Your current position is ", current_position)

    return current_position   #return value here -> current_position = move_player(current_position, roll)

# actual execution will start from here
print("lets start the game! Reach position 100 to win")

current_position = 0

while current_position < 100:
    user_choice = input("\n Press Enter to roll the dice or type 'q' to quit :").lower()  # lower function Q ko q kr dega

    if user_choice == 'q':
        print("Game Over ! Your final position was :", current_position)
        break

    roll = roll_dice()
    current_position = move_player(current_position, roll)

    if current_position >= 100:
        print("congratulations! You won") 






# snake ladder game with Condition : game tab hi strat hoga jab dice roll hoke starting me 1 or 6 dega

# Snake ladder game 
# Module / libraries used - (1) random,  (2) time 
'''
# time module
import time
print("Hello world!")
time.sleep(3)         # Delay execution for a given number of seconds.
print("This is print after 3 seconds")
time.sleep(3)
print("print after 3 seconds")
'''

import random
import time

# Step 1.
# make dictionaries for snake and ladder values

snakes = {99 : 4,         #{start : end}
         70 : 54,         #{high -> low}
         52 : 40,
         24 : 10
         }

ladders = {6 : 25,        #{low -> high}
           11 : 45,
           60 : 84,
           46 : 90
           } 

# step 2.
# define a dice and its function

def roll_dice():
    return random.randint(1, 6)   # 6 is included

# Condition : game tab hi strat hoga jab dice roll hoke starting me 1 or 6 dega
while True:
    roll = roll_dice()
    print(f"You rolled a {roll}")
    if roll == 1 or roll == 6:
        current_position = roll
        print(f"Game started! You are at position {current_position}")
        break
    else:
        print("You need to roll a 1 or 6 to start. Try again.")
        input("Press Enter to roll again...")


# step 3.
# define how player moves
def move_player(current_position, roll):
    print("You rolled a ", roll, "!")
    time.sleep(2)
    current_position += roll

# step 4.
# define conditions for all the posibility in the game
# 1st -> snake byte ( drop - kon se position se kitne number par drop hoga)
# 2nd -> ladders (up - kon se point se litna upar jayenge)
# 3rd -> else(no snake, no ladder), simply print the current position

    if current_position in snakes:
        print("Oh no! It's a snake bite! Go back from", current_position, "to", snakes[current_position])
        current_position = snakes[current_position]
        print("Your current position is ", current_position)

    elif current_position in ladders:
        print("Yay! Climed a ladder from", current_position, "to", ladders[current_position])
        current_position = ladders[current_position]
        print("Your current position is ", current_position)

    else:
        print("Your current position is ", current_position)

    return current_position   #return value here -> current_position = move_player(current_position, roll)

# actual execution will start from here
print("lets start the game! Reach position 100 to win")

current_position = roll

while current_position < 100:
    user_choice = input("\n Press Enter to roll the dice or type 'q' to quit :").lower()  # lower function Q ko q kr dega

    if user_choice == 'q':
        print("Game Over ! Your final position was :", current_position)
        break

    roll = roll_dice() 
    current_position = move_player(current_position, roll)

    if current_position >= 100:
        print("congratulations! You won") 