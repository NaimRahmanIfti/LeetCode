class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1, m2 = {}, {}

        for i in range(len(s)):

            if s[i] not in m1:
                m1[s[i]] = i
            if t[i] not in m2:
                m2[t[i]] = i

            if m1[s[i]] != m2[t[i]]:
                return False
        return True

s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))