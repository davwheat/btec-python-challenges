import os
from random import choice

# Prints the chosen word at the start of the
# game for testing purposes
DEBUG_MODE = False

# Fix for VS Code workspaces
os.chdir(os.path.dirname(os.path.realpath(__file__)))

guessable_words = []
current_word = ""
current_guessed = ""
guessed_chars = []

hangmanPics = [
    r"",
    r"""
    
    
    
    
    
    
=========""",
    r"""
    
     |
     |
     |
     |
     |
=========""",
    r"""
    
     |
     |
     |
     |
    /|
=========""",
    r"""
 +---+
     |
     |
     |
     |
    /|
=========""",
    r"""
 +---+
    \|
     |
     |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
     |
     |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
     |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
 |   |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
/|   |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
/|\  |
     |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
/|\  |
/    |
    /|
=========""",
    r"""
 +---+
 |  \|
 O   |
/|\  |
/ \  |
    /|
=========""",
]

lives_remaining = len(hangmanPics) - 1

# Get list of guessable words from text file
with open("possible_words.txt", "r") as file:
    lines = file.readlines()

    for l in lines:
        # Get rid of the new lines at the end, as well as
        # any whitespace
        stripped = l.strip().rstrip()

        # don't add any blank lines, or lines starting with # (commented)
        if not (len(stripped) == 0 or stripped.startswith("#")):
            guessable_words += [stripped.lower()]

current_word = choice(guessable_words)
current_guessed = "?" * len(current_word)

if DEBUG_MODE:
    print("## DEBUG MODE ACTIVATED ##")
    print(f"CHOSEN WORD: {current_word}\n\n")

while lives_remaining != 0:
    # No more missing chars? They've solved it!
    if current_guessed.find("?") == -1:
        break

    print(f"Guess my word  |  You have {lives_remaining} lives remaining")
    print(hangmanPics[len(hangmanPics) - lives_remaining - 1])
    print(current_guessed)
    print()
    # Make sure input is a lowercase string with no leading or trailing whitespace!
    guess = str(input("Guess a letter, or the whole word: ")).lower().strip().rstrip()

    # region Validation
    if guess in guessed_chars:
        print("You've already guessed this letter!")
        continue

    if len(guess) == 0:
        print("Invalid guess. Please only enter one character.")
        continue

    if not guess.isalpha():
        print("Invalid guess. Please only enter alphabet letters (a-z).")
        continue
    # endregion

    if len(guess) > 1:
        # whole word guess
        if guess == current_word:
            break
        else:
            print(f"Sorry, the word isn't {guess}")
            lives_remaining -= 1
            continue

    if guess in current_word:
        # guessed letter in the word
        print("Great guess!")
        index = current_word.find(guess)

        # convert string to list to enable rewriting of char via index
        temp_word_list = list(current_guessed)
        temp_word_list[index] = current_word[index]

        current_guessed = "".join(temp_word_list)
    else:
        # guessed letter NOT in the word
        print(f"\nThe letter {guess} isn't in my word.")
        lives_remaining -= 1

if lives_remaining == 0:
    print("\nOh no! You ran out of lives!")
    print(f"My word was {current_word}")
else:
    print("\nCongratulations! You guessed the word!")
