'''
Created on Feb 27, 2018

@author: grekz
'''

class E191_Numberof1Bits:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while (n != 0):
            res += n & 1
            n >>= 1
        return res
        