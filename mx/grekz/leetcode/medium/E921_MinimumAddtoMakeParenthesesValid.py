'''
@author: grekz
'''


class E921_MinimumAddtoMakeParenthesesValid:

    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, bal = 0, 0
        for x in S:
            bal += 1 if x == '(' else -1
            if bal == -1:
                res += 1
                bal += 1
        return bal + res
