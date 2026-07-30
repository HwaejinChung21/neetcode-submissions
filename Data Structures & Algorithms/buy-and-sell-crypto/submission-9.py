class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1

            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1

        return maxProfit