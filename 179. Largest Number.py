class Solution:
    def largestNumber(self, nums):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a = str(nums[i]) + str(nums[j])
                b = str(nums[j]) + str(nums[i])

                if a > b:
                    j += 1
                elif b > a:
                    nums[i], nums[j] = nums[j], nums[i]
            if i ==0 and nums[i] == 0:
                return '0'

        return ''.join(map(str, nums))


nums = [0, 0]
print(Solution().largestNumber(nums))
#

