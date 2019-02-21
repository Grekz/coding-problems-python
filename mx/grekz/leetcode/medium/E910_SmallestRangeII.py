'''
@author: grekz
'''


class E910_SmallestRangeII:

    def smallestRangeII(self, A: 'List[int]', K: 'int') -> 'int':
        A.sort()
        n = len(A) - 1
        res = A[n] - A[0]
        for i in range(n):
            a, b = A[i], A[i+1]
            h = max(A[n] - K, a + K)
            l = min(A[0] + K, b - K)
            res = min(res, h - l)
        return res
