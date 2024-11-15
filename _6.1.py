import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 3 - math.log(abs(x - 6)) + math.cos(x)

values_for = []
for x in range(int(a * 100), int(b * 100), int(h * 100)):
    x /= 100 
    values_for.append((x, f(x)))

print("Calculation results (for loop):")
for x, fx in values_for:
    print(f"x = {x:.2f}, f(x) = {fx:.2f}")

