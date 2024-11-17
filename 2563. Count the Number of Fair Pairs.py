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

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        pairs = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] > upper:
                    j -= 1
                elif nums[i] + nums[j] >= lower:
                    i -= 1
            pairs += j - i


        return pairs // 2
nums = [0,1,7,4,4,5]
lower = 3
upper = 6
print(Solution().countFairPairs(nums, lower, upper))

# nums.sort()
# pairs = 0
# n = len(nums)
# left = right = n - 1
# for i, val in enumerate(nums):
#     while right >= 0 and val + nums[right] > upper:
#         right -= 1
#     while left >= 0 and val + nums[left] >= lower:
#         left -= 1
#     pairs += right - left
#     if left < i <= right:
#         pairs -= 1
#
# return pairs // 2