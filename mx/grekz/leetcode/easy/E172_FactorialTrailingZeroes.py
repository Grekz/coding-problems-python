'''
Created on Feb 23, 2018

@author: grekz
'''

class E172_FactorialTrailingZeroes:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
        