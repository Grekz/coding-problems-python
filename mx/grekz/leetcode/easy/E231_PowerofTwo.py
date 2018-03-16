'''
@author: grekz
'''

class E231_PowerofTwo:

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n < 1 ) : return False
        hasOne = False
        for i in range(32) :
            if( (n & 1) == 1 ):
                if(hasOne) :
                    return False
                else: 
                    hasOne = True
            n >>= 1
        return True
        