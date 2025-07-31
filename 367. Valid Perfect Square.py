class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = num
        while i * i > num:
            i = (i + num // i) //2
        return i * i == num

    # Time: O(n)
    # Space: O(n)
num = 16
print(Solution.isPerfectSquare(num))
