'''
Created on Feb 10, 2018

@author: grekz
'''

class E121_BestTimetoBuyandSellStock:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 2147483647
        result = 0
        for stockPrice in prices :
            if(stockPrice < buy):
                buy = stockPrice
            elif ( result < stockPrice - buy ) :
                result = stockPrice - buy
        return result