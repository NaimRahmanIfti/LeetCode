class Solution:
    def lengthOfLastWord(self, s):
        # return len(s.split()[-1])

        length = 0
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            length += 1
        return length


s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))

