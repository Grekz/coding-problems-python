'''
Created on Dec 6, 2017
https://leetcode.com/problems/reverse-integer/
@author: grekz
'''
class E007_ReverseInteger:    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        res  = int(str(x*sign)[::-1])
        return sign * res if  res < 2**31 else 0
        