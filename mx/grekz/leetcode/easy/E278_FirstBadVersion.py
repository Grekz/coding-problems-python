'''
@author: grekz
'''
class E278_FirstBadVersion:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1 
        r = n 
        m = 0
        while ( l < r ) :
            m = l + ( r - l ) // 2
            if ( isBadVersion(m) ):
                r = m
            else :
                l = m + 1
        return l
        