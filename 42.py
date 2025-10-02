text = input("Enter a string: ") #added input
max_char = max(text, key=text.count)
print("Most Frequent Character:", max_char)
