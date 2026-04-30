class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]  # cheapest price seen so far
        maxProfit = 0         # best profit seen so far

        for price in prices:
            if price< minPrice:
                minPrice = price
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit
            # is selling today more profitable than maxProfit?