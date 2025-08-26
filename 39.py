nums = [1, 2, 3, 4]
cumulative = []
s = 0
for n in nums:
    s += n
    cumulative.append(s)
print("Cumulative Sum:", cumulative)