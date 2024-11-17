class Solution(object):
    def rotate(self, nums, k):
        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1
        # return nums

        arr = []

        start = len(nums) - k
        arr.append(nums[start])
        i = start + 1
        while (True):
            if (i == start):
                break

            if (i > len(nums) - 1):
                i = 0

            arr.append(nums[i])
            i += 1

        return arr

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))


