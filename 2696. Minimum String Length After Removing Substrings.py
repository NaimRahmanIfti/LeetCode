s = "ABFCACDB"
stack = []
def min_len(s):
    for char in s:
        if char == 'B' and stack[-1] == 'A' or char == 'D' and stack[-1] == 'C':
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

print(min_len(s))