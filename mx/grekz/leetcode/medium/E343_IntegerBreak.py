'''
@author: grekz
'''
class E343_IntegerBreak:
    def integerBreak(self, n: int) -> int:
        if( n == 2 ) : return 1
        if( n == 3 ) : return 2
        res = 1
        while n > 4 :
            res *= 3
            n -= 3
        res *= n
        return res