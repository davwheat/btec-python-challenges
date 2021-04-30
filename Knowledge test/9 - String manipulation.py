# Store your whole name as a string. Now use slicing to write out, on different lines:
#
# - The first letter
# - The last letter
# - The middle three letters

name = "David Wheatley"

print(name[0])
print(name[-1])
print(name[len(name) // 2 - 1 : len(name) // 2 + 2])
