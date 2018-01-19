'''
Created on Jan 19, 2018

@author: grekz
'''

class E032_LongestValidParentheses:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == None or len(s) < 2) : return 0
        res = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if (s[i] == '('):
                stack.append(i)
            else:
                stack.pop()
                if (stack != []):
                    res = max(res, i - stack[len(stack)-1] )
                else:
                    stack.append(i)
        return res
        
        