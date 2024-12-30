class Solution:
    def checkString(self, s):
        s = list("".join(s))
        n = len(s)

        for i in range(n - 1):
            if s[i] == 'b' and s[i + 1] == 'a':
                return False
            i += 1
        return True


s = "abab"
print(Solution().checkString(s))



