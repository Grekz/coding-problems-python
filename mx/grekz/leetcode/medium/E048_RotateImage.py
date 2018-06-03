'''
@author: grekz
'''
class E048_RotateImage:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
                
        for i in range(n):
            for j in range(n//2):
                t = matrix[i][j]
                matrix[i][j] = matrix[i][ n - 1 - j]
                matrix[i][n - 1 - j ] = t