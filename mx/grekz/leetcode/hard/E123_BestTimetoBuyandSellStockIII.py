'''
@author: grekz
'''
class E123_BestTimetoBuyandSellStockIII:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profitA, buyA = 0, -2147483648
        profitB, buyB = 0, buyA
        for i, cur in enumerate(prices) :
            if i > 2 :
                profitB = max(profitB, buyB + cur)
            if i > 1 :
                buyB = max(buyB, profitA - cur)
            profitA = max(profitA, buyA + cur)
            buyA = max(buyA,-cur)
        return max(profitA, profitB)
            