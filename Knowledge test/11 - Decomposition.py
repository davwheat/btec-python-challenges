# Read the problem below and then implement it in code. You do not need to submit your
# written decomposition of how you’ve worked it out but make sure to comment your code
# to explain what you’ve done.
#
# A computer generates a random number from 0 – 10.  It then asks the user to make a
# guess. They have 5 attempts to get it right. If they get it correct, the program says
# they’ve won and ends. If they’re wrong, they’re asked to guess again and told how many
# attempts they have remaining.

from random import randint

# Inclusive
random_num = randint(0, 10)
turns = 5

# 5 turns
for turn in range(turns - 1, 0, -1):
    guess = int(input("Make a guess: "))

    if (guess == random_num):
        print("You're correct!")
        break
    else:
        print(f"Incorrect guess. You have {turn} guesses remaining.")
