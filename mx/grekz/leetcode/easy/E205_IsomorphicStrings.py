'''
Created on Mar 5, 2018

@author: grekz
'''

class E205_IsomorphicStrings:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if ( n != len(t) ) : return False
        a = [-1] * 256
        b = [-1] * 256
        for i in range(n) :
            si = ord(s[i])
            ti = ord(t[i])
            if ( a[si] != b[ti] ) : return False
            a[si] = b[ti] = i
        return True
        