class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)
solution = Solution()

nums1 = [3,2,2,3]
val1 = 3
print(solution.removeElement(nums1, val1))

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(solution.removeElement(nums2, val2))

nums3 = [3, 3, 3]
val3 = 3
print(solution.removeElement(nums3, val3))