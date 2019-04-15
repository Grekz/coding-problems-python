'''
@author: grekz
'''
class E0931_MinimumFallingPathSum:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(n-2, -1, -1) :
            for j in range(n):
                b = A[i+1][j]
                if j > 0 :
                    b = min( b, A[i+1][j-1] ) 
                if j+1 < n :
                    b = min( b, A[i+1][j+1] )
                A[i][j] += b
        res = 2147483647
        for x in A[0] :
            res = min(res, x)
        return res