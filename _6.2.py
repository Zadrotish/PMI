import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 3 - math.log(abs(x - 6)) + math.cos(x)

values_while = []
x = a
while x <= b:
    values_while.append((x, f(x)))
    x += h

print("\nCalculation results (while loop):")
for x, fx in values_while:
    print(f"x = {x:.2f}, f(x) = {fx:.2f}")
