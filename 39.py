def cumulative_sum(numbers):
    cumulative = []
    total = 0
    for num in numbers:
        total += num
        cumulative.append(total)
    return cumulative


input_str = input("Enter numbers separated by spaces: ")

try:
    numbers = list(map(int, input_str.strip().split()))
    result = cumulative_sum(numbers)

    print("Original list:", numbers)
    print("Cumulative sum:", result)
except ValueError:
    print("Please enter only valid integers separated by spaces.")

