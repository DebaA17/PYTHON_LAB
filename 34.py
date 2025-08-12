# Python program to print all odd numbers in a range

start, end = map(int, input("Enter start and end (space-separated): ").split())
odd_nums = [n for n in range(start, end + 1) if n % 2 == 1]
print(odd_nums)
