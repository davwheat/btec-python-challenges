# A user needs to input a number but it must be above 0 and below 100.

# Write a program that will check whether the number is in the correct range.
# If it is, tell them they’re correct otherwise tell them whether the number
# is too high or too low.

num = float(input("Enter num: "))

if (num >= 100):
    print("Too high")
elif (num <= 0):
    print("Too low")
else:
    print("Just right!")
