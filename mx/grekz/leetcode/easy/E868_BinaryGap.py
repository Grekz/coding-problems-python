'''
@author: grekz
'''


class E868_BinaryGap:

    def binaryGap(self, N: 'int') -> 'int':
        res, l = 0, -1
        for i in range(32):
            if ((N >> i) & 1) > 0:
                if l >= 0:
                    res = max(res, i - l)
                l = i
        return res
