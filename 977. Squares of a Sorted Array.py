class Solution:
    def sortedSquares(self, nums):

        # n = len(nums)
        # num = []
        # for i in range(n):
        #     num.append(nums[i] ** 2)
        # return sorted(num)
        num = []

        for i in nums:
            num.append(i*i)
        num.sort()
        return num
nums = [-4, 1, 0, 3, 10]
print(Solution().sortedSquares(nums))