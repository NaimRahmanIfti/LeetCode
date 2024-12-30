class Solution:
    def fourSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
        nums.sort()
        print(nums)
        n = len(nums)
        result = []

        for i in range(n - 3):

            for j in range(i + 1, n - 2):

                left = j + 1
                right = n - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left > right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                        # right -= 1
                    elif four_sum > target:
                        right -= 1
                        # left += 1

        answer = []
        for x in result:
            if x not in answer:
                answer.append(x)
        return answer
nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
print(Solution().fourSum(nums, target))