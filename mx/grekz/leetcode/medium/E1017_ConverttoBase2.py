'''
@author: grekz
'''
class E1017_ConverttoBase2:
    def baseNeg2(self, N: int) -> str:
        res = ""
        while N != 0:
            res = str( N & 1 ) + res
            N = -( N >> 1 )
        return res if len(res) else "0"