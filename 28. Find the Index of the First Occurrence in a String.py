class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # try:
        #     i = haystack.index(needle)
        #     return i
        # except:
        #     return -1

        for i in range(len(haystack)):
            j = 0
            for k in range(i, len(haystack)):
                if haystack[k] == needle[j]:
                    j += 1
                else:
                    break
                if j == len(needle):
                    return i

        return -1
haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))