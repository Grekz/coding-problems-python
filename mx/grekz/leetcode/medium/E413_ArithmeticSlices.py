'''
@author: grekz
'''


class E413_ArithmeticSlices:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        tmp, res, n = 0, 0, len(A)
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                tmp += 1
                res += tmp
            else:
                tmp = 0
        return res
