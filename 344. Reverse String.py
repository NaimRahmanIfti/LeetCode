class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n - i - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


s = ["h","e","l","l","o"]
print(Solution().reverseString(s))
