'''
@author: grekz
'''


class E392_IsSubsequence:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = -1
        for c in s:
            idx = t.find(c, idx + 1)
            if idx == -1:
                return False
        return True
