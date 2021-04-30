# Ask the user to enter a word. Have the program keep asking them to
# enter one while the user writes "continue" as their word.

keyword = "continue"
current_word = ""

while current_word == keyword:
    current_word = input("Enter a word: ").strip()
