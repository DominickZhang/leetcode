class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        max_value = 0
        i = 0; j = 1
        while j < n:
            if prices[j] - prices[i] <= 0:
                i = j
                j += 1
            else:
                if prices[j] - prices[i] > max_value:
                    max_value = prices[j] - prices[i]
                j += 1
        return max_value