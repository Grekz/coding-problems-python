'''
@author: grekz
'''
class E1012_ComplementofBase10Integer:
    def bitwiseComplement(self, N: int) -> int:
        a = 1
        while ( a < N ) : a = a * 2 + 1
        return a - N