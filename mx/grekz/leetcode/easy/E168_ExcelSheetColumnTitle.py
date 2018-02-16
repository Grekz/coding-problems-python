'''
Created on Feb 16, 2018

@author: grekz
'''

class E168_ExcelSheetColumnTitle:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if ( n == 0 ): return ""
        res = ""
        ordA = ord('A')
        while ( n > 0 ) :
            n -= 1
            res = chr( ordA + n%26 ) + res
            n //=26
        return res
        
        