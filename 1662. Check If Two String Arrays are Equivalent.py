class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        word1 = "".join(word1)
        word2 = "".join(word2)

        return True if word1 == word2 else False

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(Solution().arrayStringsAreEqual(word1, word2))

