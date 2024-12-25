class Solution:
    def majorityElement(self, nums):
        h1 = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in h1:
                h1[nums[i]] += 1
            else:
                h1[nums[i]] = 1

        for x in h1:
            if h1[x] > n/2:
                return x


nums = [6,5,5]
print(Solution().majorityElement(nums))



