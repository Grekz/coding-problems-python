'''
@author: grekz
'''
class E240_Searcha2DMatrixII:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not len(matrix): return False
        r, c, rs = 0, len(matrix[0]) -1, len(matrix)
        while r < rs and c > -1 :
            cur = matrix[r][c]
            if cur == target : return True
            if cur < target :
                r += 1
            else:
                c -= 1
        return False