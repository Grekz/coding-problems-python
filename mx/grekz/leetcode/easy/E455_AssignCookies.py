'''
@author: grekz
'''
class E455_AssignCookies:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        gi = si = 0
        gn = len(g)
        sn = len(s)
        while gi < gn and si < sn :
            if g[gi] <= s[si] :
                gi+=1
            si+=1
        return gi