class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        #
        # for i in range(k):
        #     current_sum += nums[i]
        # max_avg = current_sum / k
        #
        # for i in range(k, n):
        #     current_sum += nums[i]
        #     current_sum -= nums[i-k]
        #
        #     current_avg = current_sum / k
        #     max_avg = max(max_avg, current_avg)
        #
        # return max_avg
        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        for i in range(k, n):
            current_sum += nums[i]
            current_sum -= nums[i - k]
            current_avg = current_sum / k
            max_avg = max(max_avg, current_avg)
        return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))
