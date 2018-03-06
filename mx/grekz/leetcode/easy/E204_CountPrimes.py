'''
Created on Mar 6, 2018

@author: grekz
'''

class E204_CountPrimes:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if ( n < 3 ) : return 0
        if n == 3 : return 1
        tmp = [False] * ( n + 1 )
        i = 2
        while i * i <= n:
            if not tmp[i] :
                j = i * 2
                while j <= n :
                    tmp[j] = True
                    j += i
            i+=1
        res = -2
        for x in tmp[:-1] :
            if not x :
                res += 1
        return res
        