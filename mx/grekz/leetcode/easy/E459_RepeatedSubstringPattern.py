'''
@author: grekz
'''
class E459_RepeatedSubstringPattern:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in ( s + s )[1:-1]