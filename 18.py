def sum_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_natural_numbers(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Please enter a positive integer.")
        else:
            print(f"Sum of natural numbers up to {num} is {sum_natural_numbers(num)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
