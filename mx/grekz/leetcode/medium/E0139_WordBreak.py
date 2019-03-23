'''
@author: grekz
'''
class E0139_WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        f = [False] * n
        f[0] = True
        for i in range( 1, n ) :
            for j in range( i ) :
                if f[j] and s[j:i] in wordDict :
                    f[i] = True
                    break
        return f[n - 1]