'''
@author: grekz
'''
class E0714_BestTimetoBuyandSellStockwithTransactionFee:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a, b, c = 0, -2147483648, 0
        for x in prices :
            c = a
            a = max( a, b + x )
            b = max( b, c - fee - x)
        return a