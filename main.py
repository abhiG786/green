import math
pi = 3.141592656
formatPI = "value of PI: {: .2f}".format(math.pi)
print(formatPI)
radius = float(input("Enter the radius"))
areaCircle = math.pi * radius **2
print (f"Area of circle areaCircle {areaCircle:.4f}")