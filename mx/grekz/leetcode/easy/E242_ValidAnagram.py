'''
@author: grekz
'''
class E242_ValidAnagram:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if( len(s) != len(t) ) : return False
        tmp = [0] * 26
        for c in s :
            tmp[ord(c) - 97] +=1
            
        for c in t :
            if ( tmp[ord(c) - 97] == 0 ) :
                return False
            tmp[ord(c) - 97] -= 1
        return True