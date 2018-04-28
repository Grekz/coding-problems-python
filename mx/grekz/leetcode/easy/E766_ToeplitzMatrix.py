'''
@author: grekz
'''
class E766_ToeplitzMatrix:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        for i in range(0, m) :
            for j in range (0, n) :
                if ( matrix[i][j] != matrix[i+1][j+1] ):
                    return False
        return True