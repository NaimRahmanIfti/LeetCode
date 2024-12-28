class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
       """

        for i in range(m , m + n):
            for j in range(n):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    nums2.remove(nums2[j])
                    break

        for x in range(len(nums1)):
            for y in range(0, len(nums1) - x - 1):
                if nums1[y] >= nums1[y + 1]:
                    nums1[y], nums1[y + 1] = nums1[y + 1], nums1[y]
        return nums1


nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(Solution().merge(nums1, m, nums2, n))

