base_pay = float(input("Enter base pay (e.g. 9.50): "))
hours_worked = int(input("Enter hours worked (e.g. 35): "))

if hours_worked < 0 or hours_worked > 60:
    print("Cannot work less than 0 hours or more than 60 hours.")

wage = 0

if hours_worked <= 40:
    wage += base_pay * hours_worked
else:
    wage += base_pay * 40
    wage += base_pay * 1.5 * (hours_worked - 40)

print(f"Pay: £{wage}")
