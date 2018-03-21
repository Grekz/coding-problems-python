'''
@author: grekz
'''
class E342_PowerofFour:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1 : return False
        while num % 4 == 0 :
            num //= 4
        return num == 1
        