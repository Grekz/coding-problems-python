'''
Created on Jan 30, 2018

@author: grekz
'''
import math

class E070_ClimbingStairs:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = math.sqrt(5)
        b = math.pow( (1 + a) / 2 , n + 1)
        c = math.pow( (1 - a) / 2 , n + 1)
        return int( 1/a * ( b - c ) )
        