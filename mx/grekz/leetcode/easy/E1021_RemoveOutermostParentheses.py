'''
@author: grekz
'''
class E1021_RemoveOutermostParentheses:
    def removeOuterParentheses(self, S: str) -> str:
        c, res = 0, ""
        for x in S :
            if x == '(':
                if c > 0 :
                    res += x
                c += 1                
            if x == ')' :
                if c > 1 :
                    res += x
                c -= 1
        return res