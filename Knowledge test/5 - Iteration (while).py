# Ask the user to enter a word. Have the program keep asking them to
# enter one until the user writes "quit" as their word.

keyword = "quit"
current_word = ""

while current_word != keyword:
    current_word = input("Enter a word: ").strip()
