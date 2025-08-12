# Python program to print even numbers in a list

nums = list(map(int, input("Enter numbers (space-separated): ").split()))
even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)
