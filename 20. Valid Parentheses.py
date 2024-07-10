class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match ={")":"(","}":"{","]":"["}

        for p in s:
            if p in match.values():
                stack.append(p)
            elif stack and match[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []
