'''
Created on Feb 18, 2018

@author: grekz
'''

class E171_ExcelSheetColumnNumber:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res = res * 26 + ord(s[i]) - 64
        return res