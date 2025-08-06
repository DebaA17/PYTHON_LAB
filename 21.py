# Python program to find sum of array

n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

total = sum(arr)

print(f"Array: {arr}")
print(f"Sum of array: {total}")