# Python program to print positive numbers in a list

nums = list(map(int, input("Enter numbers (space-separated): ").split()))
positive_nums = [n for n in nums if n > 0]
print(positive_nums)