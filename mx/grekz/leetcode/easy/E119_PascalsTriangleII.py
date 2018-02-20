'''
Created on Feb 20, 2018

@author: grekz
'''

class E119_PascalsTriangleII:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex) :
            for j in range(len(res)-1, 0, -1):
                res[j] = res[j] + res[j-1]
            res += [1]
        return res