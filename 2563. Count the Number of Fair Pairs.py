class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        pairs = 0
        left, right = 0, len(nums)-1
        while left < right:
            if lower <= nums[left] + nums[right] <= upper:
                pairs += 1
                left += 1
                right -= 1
            else:
                right -= 1
        return pairs
nums = [1,7,9,2,5]
lower = 11
upper = 11
print(Solution().countFairPairs(nums, lower, upper))
