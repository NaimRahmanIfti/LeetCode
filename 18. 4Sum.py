def fourSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    n_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k + 1, len(nums)):
                    n_nums = [nums[i], nums[j], nums[k], nums[l]]
                    if sum(n_nums) == target:
                        n_nums.sort()
                        if n_nums not in n_list:
                            n_list.append(n_nums)
                            return n_list

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))