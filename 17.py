# Program to calculate the sum of squares of first n natural numbers
def sum_of_squares(n):
    return sum(i*i for i in range(1, n+1))

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of n: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            result = sum_of_squares(n)
            print(f"Sum of squares of first {n} natural numbers is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
