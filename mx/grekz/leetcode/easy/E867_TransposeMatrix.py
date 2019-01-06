'''
@author: grekz
'''


class E867_TransposeMatrix:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(A), len(A[0])
        return [[A[j][i] for j in range(n)] for i in range(m)]
