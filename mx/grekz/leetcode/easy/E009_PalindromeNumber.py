'''
Created on Dec 9, 2017

@author: grekz
'''
class E009_PalindromeNumber:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        return str(x)[::-1] == str(x)
        