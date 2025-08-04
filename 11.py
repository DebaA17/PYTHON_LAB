def find_factors(number):
    print(f"Factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

def main():
    try:
        num = int(input("Enter a number to find its factors: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            find_factors(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
