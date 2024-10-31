class Solution:
    def minSwaps(self, s):
        count = 0
        for c in s:
            if c == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    count += 1
        return (count//2)

so = Solution()
print(so.minSwaps('][][]['))







