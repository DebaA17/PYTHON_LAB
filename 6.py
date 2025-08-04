# [i] Swap using third variable
a = 5
b = 10
print("Before swap (using third variable):", a, b)
temp = a
a = b
b = temp
print("After swap:", a, b)

# [ii] Swap without using third variable
x = 15
y = 20
print("Before swap (without third variable):", x, y)
x, y = y, x
print("After swap:", x, y)
