'''
Created on Dec 5, 2017

https://leetcode.com/problems/zigzag-conversion

@author: grekz
'''
class E006_ZigZagConversion:
    def convert(self, s, rows):
        """
        :type s: str
        :type rows: int
        :rtype: str
        """
        if rows < 2:
            return s
        res = [''] * rows
        i = dire = 0
        for x in s:
            res[i] += x
            if i == 0:
                dire = 1
            elif i == rows-1:
                dire = -1
            i += dire
        return ''.join(res)