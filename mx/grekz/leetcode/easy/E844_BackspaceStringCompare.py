'''
@author: grekz
'''
class E844_BackspaceStringCompare:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.doit(S) == self.doit(T)
    
    def doit(self, s):
        n = len(s) - 1
        res = ""
        c = 0
        h = '#'
        for i in range(n, -1, -1) :
            cur = s[i]
            if cur == h :
                c += 1
            elif c > 0 :
                c -= 1
            else:
                res += cur
        return res