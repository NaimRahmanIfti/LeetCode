class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        memoization = [0, 1, 1]
        for i in range(3, n + 1):
            memoization.append(memoization[i - 1] + memoization[i - 2])
        return memoization[n]

n = 4
print(Solution().fib(n))

