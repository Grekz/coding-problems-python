'''
@author: grekz
'''
class E389_FindtheDifference:

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        r = 0
        for x in s :
            r ^= ord(x)
        for x in t :
            r ^= ord(x)
        return chr(r)