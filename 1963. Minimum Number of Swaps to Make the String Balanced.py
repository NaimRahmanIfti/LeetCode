class Solution:
    def minSwaps(self, s):
        count = 0
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                    count += 1
                else:
                    count += 1

        return round(count/2)

so = Solution()
print(so.minSwaps('][][]['))



