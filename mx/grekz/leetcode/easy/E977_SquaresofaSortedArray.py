'''
@author: grekz
'''


class E977_SquaresofaSortedArray:

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = [0] * n
        for i in range(n):
            A[i] *= A[i]
        i, j, k = 0, n-1, n-1
        while i <= j:
            if A[i] < A[j]:
                res[k] = A[j]
                j -= 1
            else:
                res[k] = A[i]
                i += 1
            k -= 1
        return res
