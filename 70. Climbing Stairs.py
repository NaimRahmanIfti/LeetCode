class Solution:
    def climbStairs(self, n: int) -> int:
        def climbway(n):
            if n == 1:
                 return 1
            if n == 2:
                return 2
        # if n >= 3:
            return climbway(n -1) + climbway(n -2)
        return climbway(n)


n = 44
print(Solution().climbStairs(n))