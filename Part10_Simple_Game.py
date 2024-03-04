import random

# Generate a random 3-digit number with no repeating digits
digits = random.sample(range(10), 3)
print(digits)

print("Welcome to Wills Games\nYou are expected to input three different digits with spaces between them.\nNotice: A correct answer is rewarded with 0.2 cedis")

while True:
    # Take user input for the guess
    guess_input = input("What is your guess? ")

    # Check if the input is valid (contains exactly three digits)
    if len(guess_input) != 3 or not guess_input.isdigit():
        print("Invalid input. Please enter three digits.")
        continue

    # Convert the input to a list of integers
    guess = [int(digit) for digit in guess_input]

    # Check if the guess is correct
    if guess == digits:
        print("Correct guess! You win 0.2 cedis.")
        break
    else:
        # Check for matching digits at the correct position
        matches = [digit == digits[i] for i, digit in enumerate(guess)]

        if any(matches):
            print("Match: You've guessed a correct number in the correct position.")
        else:
            # Check for correct digits in the wrong position
            close_matches = [digit in digits for digit in guess]

            if any(close_matches):
                print("Close: You've guessed a correct number but in the wrong position.")
            else:
                print("Nope: You haven't guessed any of the numbers correctly.")

# End the game
input("Press any key to quit")
