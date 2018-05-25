'''
@author: grekz
'''
class E062_UniquePaths:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(m-1) :
            res = res * ( i + n ) // ( i + 1 )
        return res