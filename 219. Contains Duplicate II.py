class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i, j in enumerate(nums):
            if j in h  and abs(i - h[j]) <= k:
                return True
            else:
                h[j] = i
        return False

                
            
