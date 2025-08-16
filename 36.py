# Function to print all negative numbers in a given range
def print_negative_numbers(start, end):
    print(f"Negative numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num < 0:
            print(num)

# Example usage
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print_negative_numbers(start_range, end_range)
