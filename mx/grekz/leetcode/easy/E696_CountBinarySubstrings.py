'''
@author: grekz
'''


class E696_CountBinarySubstrings:

    def countBinarySubstrings(self, s: 'str') -> 'int':
        res, p, c = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(p, c)
                p = c
                c = 1
            else:
                c += 1
        return res + min(p, c)
