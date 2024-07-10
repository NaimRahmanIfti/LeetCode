
def rotate(s, goal):
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == goal:
            return True
        elif i==len(s)-1 and s!= goal:
            return False


s = "abcde"
goal = "cdeab"
print(rotate(s, goal))
