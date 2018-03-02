'''
Created on Mar 2, 2018

@author: grekz
'''

class E202_HappyNumber:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if ( n < 1 or n == 4 ) : return False
        if ( n in [ 1, 7, 10, 13, 19, 23 ]) : return True
        res = 0
        while n > 0:
            res += (n % 10) * (n%10)
            n //= 10
        return self.isHappy(res)
      
        