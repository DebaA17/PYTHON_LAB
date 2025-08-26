sentence = "this is is a test test sentence"
words = sentence.split()
unique = []
for w in words:
    if w not in unique:
        unique.append(w)
print("Without Duplicates:", " ".join(unique))