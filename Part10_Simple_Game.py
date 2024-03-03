###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

# Another hint:
print("Welcome to Wills Games \nYou are accept to input three differnet with space between them \t NOtice correct answer is reward with 0.2 cedis")

while True:
    guess,x, y = input("What is your guess? ").split()
    lis=[int(guess),int(x),int(y)]
    

    if lis == digits[:3]:
        print("Correct guess")
        break
    elif lis[0]== digits[0] or lis[1]== digits[1] or lis[2]== digits[2]  :
        print("One of your input is correct and at the right space")
    else:
        print("Worng Guess")


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

input("Please any key to quit")


