change = float(input("Enter change to dispense: "))

# list of all values that can be dispensed
values = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

dispensed = []

for val in values:
    while change >= val:
        dispensed.append(val)
        change -= val

counter = 0
lastVal = dispensed[0]
for val in dispensed:
    if val == lastVal:
        counter += 1
    else:
        print(f"{counter} x £{lastVal}")
        lastVal = val
        counter = 1

print(f"{counter} x £{lastVal}")
lastVal = val
counter = 1
