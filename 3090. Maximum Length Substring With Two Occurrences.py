class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        empty_set = set()
        l = 0
        maximum_length = 0
        for r in range(len(s)):
            while s[r] in empty_set and s[r].count(s[r]) > 2:
                empty_set.remove(s[l])
                l += 1
            size = r - l + 1
            maximum_length = max(maximum_length, size)
            empty_set.add(s[r])
        return maximum_length

s = "bcbbbcba"
print(Solution().maximumLengthSubstring(s))

