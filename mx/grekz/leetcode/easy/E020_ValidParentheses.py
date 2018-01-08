'''
Created on Jan 8, 2018

@author: grekz
'''

class E020_ValidParentheses:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if ( s is None or len(s) < 1 ) :
            return True
        if ( len(s) == 1 ) :
            return False
        ope = "({["
        clo = ")}]"
        stack = []
        for cur in s :
            if ope.find(cur) != -1 :
                stack.append(cur)
            elif len(stack) < 1 or ope.find(stack.pop()) != clo.find(cur) :
                return False
        return len(stack) == 0
        