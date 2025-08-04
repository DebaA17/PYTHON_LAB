num = int(input("Enter the number : "))

if num < 0:
    print(f"{num} is a negative integer")
elif num > 0:
    print(f"{num} is a positive integer")
else:
    print("This is zero")
