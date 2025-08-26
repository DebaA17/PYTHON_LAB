words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}
for w in words:
    key = "".join(sorted(w))
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(w)
print("Anagram Groups:", list(anagrams.values()))