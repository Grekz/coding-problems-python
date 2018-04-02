'''
@author: grekz
'''
class E400_NthDigit:

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if ( n < 10 ) : 
            return n
        n -= 1
        digitInNumber = 1
        rangeNumber = 1
        while (n / 9 / rangeNumber / digitInNumber >= 1) :
            n -= 9 * rangeNumber * digitInNumber
            digitInNumber+=1
            rangeNumber *= 10
        res = str(rangeNumber + n/digitInNumber)
        return int(res[n%digitInNumber])