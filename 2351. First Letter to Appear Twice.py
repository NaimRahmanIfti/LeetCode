class Solution:
    def repeatedCharacter(self, s):
        seen = []

        for c in s:
            if c not in seen:
                seen.append(c)
            else:
                return c

s = "abccbaacz"
print(Solution().repeatedCharacter(s))