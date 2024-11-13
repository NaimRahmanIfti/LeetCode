class Solution:
    def replaceWords(self, dictionary, sentence):
        s = sentence.split(' ')
        for i in range(len(s)):
            for word in dictionary:
                if s[i].startswith(word):
                    s[i] = word
        return ' '.join(s)

dictionary = ["catt","cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))
