class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        new_nums = [nums[0]] # [2, 4, 1, 6, 5]

        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                new_nums.append(nums[i])

        for x in range(1, len(new_nums)- 1):
            l = x - 1
            r = x + 1
            if new_nums[x] > new_nums[l] and new_nums[x] > new_nums[r] or new_nums[x] < new_nums[l] and new_nums[x]< new_nums[r]:
                count += 1
                
        return count

nums = [2,4,1,1,6,5]
print(Solution.countHillValley(nums))
