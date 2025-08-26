tup = (123, 45, 6)
digits = []
for num in tup:
    for d in str(num):
        digits.append(int(d))
print("Digits:", digits)