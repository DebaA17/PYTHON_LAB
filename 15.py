def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Example usage:
n = int(input("Enter the position (n) to find the Fibonacci number: "))
print(f"The {n}th Fibonacci number is:", fibonacci(n))
