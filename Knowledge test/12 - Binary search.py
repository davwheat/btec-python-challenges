# Using your list from Challenge 6, ask the user for a TV show name and implement a
# binary search to inform the user whether or not the name the entered is in the
# list or not

shows = [
    "Line of Duty",
    "Will & Grace",
    "Game of Thrones",
    "Malcolm in the Middle",
    "Everybody Loves Raymond",
]
shows.sort()

print(shows)

search_key = input("Key: ")

first = 0
last = len(shows) - 1

found = False

while not found and first <= last:
    middle = (last + first) // 2
    middle_value = shows[middle]

    if middle_value == search_key:
        found = True
    elif middle_value < search_key:
        first = middle + 1
    else:
        last = middle - 1

if found:
    print("In list")
else:
    print("Not in list")
