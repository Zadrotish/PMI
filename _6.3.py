import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 3 - math.log(abs(x - 6)) + math.cos(x)

values = []
x = a
while x <= b:
    values.append((x, f(x)))
    x += h

print("\nList of values (row):")
print(values)

print("\nList of values (column):")
for x, fx in values:
    print(f"x = {x:.2f} | f(x) = {fx:.2f}")

