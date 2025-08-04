num = int(input("Enter a number: "))
n = len(str(num))
sum = sum(int(digit) ** n for digit in str(num))
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")