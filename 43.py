st = "Hello@World"
special = False
for ch in st:
    if not ch.isalnum():
        special = True
        break
print("Contains Special Character:", special)