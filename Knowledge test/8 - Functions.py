# Make a function that takes two numbers as parameters. Your function will then multiply these two
# numbers together and return the result. Write a program that will use your function to show that
# it works correctly.


def mult(x, y):
    return x * y


num1 = float(input("Num1: "))
num2 = float(input("Num2: "))

print(mult(num1, num2))
