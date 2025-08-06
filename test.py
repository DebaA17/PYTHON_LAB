# This is a test file

n = int(input("Enter the element : "))

arr =[]

print("Enter the elements : ")
for i in range(n):
    arr.append(int(input()))

total = sum(arr)

print(f"Array : {arr}")
print(f"The sum of array : {total}")