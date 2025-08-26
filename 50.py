lst = ["a", "b", "a", "c", "b", "a"]
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
print("Frequencies:", freq)