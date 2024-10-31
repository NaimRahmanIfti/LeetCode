class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1 , j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

sol = Solution()
print(sol.twoSum([2,3,4], 6))
