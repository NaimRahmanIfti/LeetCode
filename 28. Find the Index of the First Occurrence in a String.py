class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            i = haystack.index(needle)
            return i
        except:
            return -1
haystack = "hello world"
needle = "world"
print(Solution().strStr(haystack, needle))