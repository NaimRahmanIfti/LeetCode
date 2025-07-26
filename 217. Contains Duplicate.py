class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = set()
        for x in nums:
            if x not in n:
                n.add(x)
            else:
                return True
        return False
