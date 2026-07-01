class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_num = sum(nums)

        expected = n * (n + 1) //2
        missing = expected - sum_num
        return missing
