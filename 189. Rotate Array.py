class Solution(object):
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
print (Solution().rotate(nums, k))
