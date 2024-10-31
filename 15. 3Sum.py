class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        target = 0
        for i in range( len(nums)):
            if nums[i] > 0:
                break
            elif nums[i] == nums[i - 1] and i > 0:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # while j < k and nums[k] == nums[k + 1]:
                    #     k -= 1
                elif add < target:
                    j += 1
                else:
                    k -= 1
        return res

nums = [0, 0, 0, 0]
sol = Solution()
print(sol.threeSum(nums))