class Solution:
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False


s = "cat"
t = "rat"
print(Solution().isAnagram(s, t))