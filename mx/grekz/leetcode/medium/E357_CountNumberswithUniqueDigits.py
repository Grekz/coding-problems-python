'''
@author: grekz
'''


class E357_CountNumberswithUniqueDigits:
    def countNumbersWithUniqueDigits(self, n: 'int') -> 'int':
        if (n == 0):
            return 1
        if (n == 1):
            return 10
        if (n == 2):
            return 91
        res, t = 10,  9
        n = min(n, 10)
        for i in range(1, n):
            t *= 10 - i
            res += t
        return res
