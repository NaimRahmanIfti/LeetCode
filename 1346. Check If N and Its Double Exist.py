class Solution:
    def checkIfExist(self, arr):
        arr.sort()
        n = len(arr)
        left = 0
        right = n - 1
        # mid = right + left //2

        while left < right:
            if arr[left] * 2 in arr or arr[right] * 2 in arr:
                return True
            left += 1
            right -= 1
        return False



arr = [3,1,7,11]
print(Solution().checkIfExist(arr))