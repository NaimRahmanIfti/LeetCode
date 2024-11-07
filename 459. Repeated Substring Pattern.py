class Solution:
    def repeatedSubstringPattern(self, s):
        # index is starting from 1 in s and iterate till the middle of the string
        for i in range(1, len(s)//2 + 1):
            # if the reminder is 0 after divide the length of the s by the index then the first part of the s will be substring
            if len(s) % i == 0:
                substring = s[:i]
                # if substring in the last part of the s then true
                if substring in s[i:-1]:
                    return True
                else:
                    return False
s = "abac"
print(Solution().repeatedSubstringPattern(s))

