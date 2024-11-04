# class Solution:
#     def minOperations(nums, k):
#         count = 0
#         for i in range(len(nums)):
#             smallest = min(nums)
#             if smallest < k:
#                 nums.remove(smallest)
#                 count += 1
#         return count
#
# nums = [2,11,10,1,3]
# k = 10
# print(Solution.minOperations(nums, k))

"""
Another way
"""


class Solution:
    def minOperations(self, nums, k):
        return len([i for i in nums if i < k])

nums = [2,11,10,1,3]
k = 10
print(Solution.minOperations(nums, k))