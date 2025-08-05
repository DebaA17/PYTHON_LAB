def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of terms: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"Fibonacci sequence up to {num} terms:")
            print(fibonacci(num))
    except ValueError:
        print("Invalid input. Please enter an integer.")
