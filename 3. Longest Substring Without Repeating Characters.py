class Solution:
    def lengthOfLongestSubstring(self, s):
        empty_set = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in empty_set:
                empty_set.remove(s[l])
                l += 1

            size = (r - l) + 1

            longest = max(longest, size)
            empty_set.add(s[r])
        return longest
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))


