class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original_number = x
        reverse_number = 0

        while x > 0:
            reminder = x % 10
            reverse_number = reverse_number * 10 + reminder
            x = x // 10
        return original_number == reverse_number
