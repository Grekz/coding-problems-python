'''
@author: grekz
'''
class E856_ScoreofParentheses:
    def scoreOfParentheses(self, S: str) -> int:
        prev = bal = res = 0
        for c in S :
            if ( c == '('):
                bal+=1
            else:
                bal-=1
                if ( prev == '(') :
                    res += 1 << bal
            prev = c
        return res