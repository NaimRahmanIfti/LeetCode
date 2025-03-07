class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_arr = []

        for i in nums1:
            for j in nums2:
                if i not in new_arr and i == j:
                    new_arr.append(i)
        return new_arr
