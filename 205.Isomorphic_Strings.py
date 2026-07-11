class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in h1 and h1[s[i]] != t[i]:
                return False
            if t[i] in h2 and h2[t[i]] != s[i]:
                return False
            h1[s[i]] = t[i]
            h2[t[i]] = s[i]
        return True

            



