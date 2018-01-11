'''
Created on Jan 11, 2018

@author: grekz
'''

class E022_GenerateParentheses:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def btHelper(st, ope, clo, res):
            if ( ope > 0) :
                btHelper(st + "(", ope - 1, clo, res)
            if ( clo > ope ) :
                btHelper(st + ")", ope, clo - 1, res)
            if ( clo < 1 ) :
                res.append(st)
            return res
        return btHelper("",n,n,[])