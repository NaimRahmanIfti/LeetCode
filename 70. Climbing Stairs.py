class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 1
        for i in range(3, n+1):
            a, b = b, a+b
            if i == n:
                return b
        return b



n = 44
print(Solution().climbStairs(n))