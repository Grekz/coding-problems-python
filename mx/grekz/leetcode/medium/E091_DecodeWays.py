'''
@author: grekz
'''


class E091_DecodeWays:

    def numDecodings(self, s: 'str') -> 'int':

        if not s or not len(s) or s[0] == '0':
            return 0
        res = [1, 1]
        for i in range(2, len(s) + 1):
            res.append(0)
            if s[i-1] != '0':
                res[i] += res[i-1]

            if s[i-2] == '1' or (s[i-2] == '2' and ord(s[i-1]) < 55):
                res[i] += res[i-2]

        return res[-1]
