'''
Created on Feb 19, 2018

@author: grekz
'''

class E118_PascalsTriangle:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        for i in range(numRows):
            for j in range(len(cur)-1, 0, -1):
                cur[j] = cur[j] + cur[j-1]
            cur += [1]
            res.append(cur[:])
        return res
        