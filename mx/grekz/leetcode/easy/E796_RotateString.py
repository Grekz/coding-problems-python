'''
@author: grekz
'''
class E796_RotateString:

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A+A