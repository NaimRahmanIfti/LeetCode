import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] <= target:
                    i = bisect.bisect_left(nums, target)
                    return i
                if nums[i] >= target:
                    i = bisect.bisect_right(nums, target)
                    return i