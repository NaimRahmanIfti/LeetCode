class Solution:
    def isBalanced(self, num):
        num = list(map(int, num))

        even_sum = 0
        odd_sum = 0
        for i in range(len(num)):
            if i % 2 == 0: #sum of even index
                even_sum += num[i]
            else:       # sum of odd index
                odd_sum += num[i]
        return even_sum == odd_sum

num = "1234"
print(Solution().isBalanced(num))