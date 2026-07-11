class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        best = len(nums) + 1

        for i in range(len(nums)):
            cur_sum += nums[i]
            
            while cur_sum >= target:
                win_size = i - left + 1
                best = min(best, win_size)
                cur_sum -= nums[left]
                left += 1
        if best == len(nums) + 1:
            return 0  
        return best
                





