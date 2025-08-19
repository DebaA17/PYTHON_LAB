def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

try:
    n = int(input("Enter the position (starting from 0): "))
    print("Fibonacci number at position", n, "is:", fibonacci(n))
except ValueError:
    print("Please enter a valid integer.")

