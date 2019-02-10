'''
@author: grekz
'''


class E201_BitwiseANDofNumbersRange:

    def rangeBitwiseAnd(self, m: 'int', n: 'int') -> 'int':
        while m < n:
            n &= n-1
        return n
