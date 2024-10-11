def multiplication( num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] * num [j] == target:
                return i, j
    return []

num = [1, 2, 3, 4, 5]
target = 12
print(multiplication(num, target))