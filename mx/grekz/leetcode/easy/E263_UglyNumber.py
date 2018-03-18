'''
@author: grekz
'''
class E263_UglyNumber:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num == 0 or num == 14) : return False
        if (num == 1 or num == 6 or num == 8) : return True
        if ( num % 5 == 0) : return self.isUgly(num // 5)
        if ( num % 3 == 0) : return self.isUgly(num // 3)
        if ( num % 2 == 0) : return self.isUgly(num // 2)
        return False