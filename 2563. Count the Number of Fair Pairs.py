class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        pairs = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if lower <= total <= upper:
                k = right
                while left < k and lower <= nums[left] + nums[k] <= upper:
                    pairs += 1
                    k -= 1
                left += 1
            elif total < lower:
                left += 1
            else:
                right -= 1

        return pairs


nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(Solution().countFairPairs(nums, lower, upper))

