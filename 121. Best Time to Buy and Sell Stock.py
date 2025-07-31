class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        p = len(prices)

        for i in range(1, p):
            if prices[i] < buy:
                buy = prices[i]

            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
    # Time: O(n) {LEngth of the prices array}
    # Space: O(n) {a constant amount of extra space is used}
            

prices = [7,1,5,3,6,4]
print(Solution.maxProfit(prices))
