'''
@author: grekz
'''
class E507_PerfectNumber:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if ( num < 2 ) : return False
        if (num == 6 or num == 28 or num == 496 ) : return True
        res = 1 
        sqrt = int(num**0.5)
        for i in range(2, sqrt+1):
            if ( num % i == 0 ):
                res += i + num // i
        return num == res