'''
@author: grekz
'''
class E010_RegularExpressionMatching:
    def isMatch(self, s: str, p: str) -> bool:
        tn, pn = len(s), len(p)
        dp = [[False] * (pn + 1) for _ in range(tn+1) ]
        dp[tn][pn] = True
        for i in range(tn, -1, -1):
            for j in range(pn - 1, -1, -1):
                fm = bool( i < tn and ( s[i] == p[j] or p[j] == '.' ) )
                if ( j + 1 < pn and p[j+1] == '*' ) :
                    dp[i][j] = dp[i][j+2] or fm and dp[i+1][j]
                else:
                    dp[i][j] = fm and dp[i+1][j+1]
        return dp[0][0]