guessable_words = []

# Get list of guessable words from text file
with open('./possible_words.txt', 'r') as file:
    lines = file.readlines()

    for l in lines:
        # Get rid of the new lines at the end, as well as
        # any whitespace
        stripped = l.rstrip()

        # don't add any blank lines, or lines starting with # (commented)
        if not( len(stripped) == 0 or stripped.startswith("#")):
            guessable_words += [stripped]

print(guessable_words)