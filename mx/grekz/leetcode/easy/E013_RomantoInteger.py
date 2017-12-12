'''
Created on Dec 12, 2017

@author: grekz
'''
class E013_RomantoInteger:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        res = 0
        val = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for x in s :
            t.append(val[x])
        for i, e in enumerate(t[:-1]) :
            res += ( -1 if e < t[i+1] else 1 ) * e
        return res + t[-1]
                