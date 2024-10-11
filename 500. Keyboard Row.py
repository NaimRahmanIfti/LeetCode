r1 = "qwertyuiop"
r2 = "asdfghjkl"
r3 = "zxcvbnm"
words = ["Hello", "Alaska", "Dad", "Peace"]
new_l = []

for word in words:
    words = set(words)
    word = word.lower()
    if all(word in r1 for word in word) or all(word in r2 for word in word) or all(word in r3 for word in word):
        new_l.append(word)
print(new_l)