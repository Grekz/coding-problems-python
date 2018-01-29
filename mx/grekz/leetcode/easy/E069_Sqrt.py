'''
Created on Jan 29, 2018

@author: grekz
'''

class E069_Sqrt:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while ( r * r > x ) :
            r = ( r + x / r ) // 2
        return int(r)
