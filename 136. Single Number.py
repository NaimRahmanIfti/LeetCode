class Solution:
    def singleNumber(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
nums = [2,2,1]
print(Solution().singleNumber(nums))
