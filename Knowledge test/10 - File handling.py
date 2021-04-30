# You will find a text file attached to the test called names.txt. Download a copy to the
# same folder as where you are writing your programs.
#
# The file has a name on each line. Write a program that will say “Hello” then a name for
# each one in the file.

lines = []

with open("names.txt", "r") as f:
    lines = f.readlines()

for name in lines:
    # Without strip, it'll add another new line to the end
    print(f"Hello {name.strip()}")
