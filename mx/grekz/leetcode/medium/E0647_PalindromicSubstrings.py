'''
@author: grekz
'''
class E0647_PalindromicSubstrings:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        m = 2 * n
        for i in range(m) :
            l = i // 2
            r = l + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                r += 1
                l -= 1
        return res