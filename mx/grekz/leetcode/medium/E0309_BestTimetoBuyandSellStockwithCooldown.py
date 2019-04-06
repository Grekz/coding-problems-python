'''
@author: grekz
'''
class E0309_BestTimetoBuyandSellStockwithCooldown:
    def maxProfit(self, prices: List[int]) -> int:
        a,b,c = 0,0, -2147483648
        for price in prices:
            d = b
            b = max(b, c + price)
            c = max(c, a - price)
            a = d
        return b