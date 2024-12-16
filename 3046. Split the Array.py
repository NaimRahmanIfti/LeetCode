class Solution:
    def isPossibleToSplit(self, nums):

        # for i in nums:
        #     if nums.count(i) > 2:
        #         return False
        # return True

        frequency={}
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
                if frequency[i] > 2:
                    return False
        return True

nums = [1, 1, 2, 2, 3, 4]
print(Solution().isPossibleToSplit(nums))