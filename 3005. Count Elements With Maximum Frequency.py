class Solution:
    def maxFrequencyElements(self, nums):

        freq = []
        max_freq = 0
        for i in nums:

            if nums.count(i) > max_freq:
                freq = []
                freq.append(i)
                max_freq = nums.count(i)
                continue
            if nums.count(i) == max_freq:
                freq.append(i)

        return len(freq)

nums = [10, 12, 11, 9, 6, 19, 11]
print(Solution().maxFrequencyElements(nums))





