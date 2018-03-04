'''
Created on Mar 4, 2018

@author: grekz
'''

class E405_ConvertaNumbertoHexadecimal:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if ( num == 0 ) : return "0"
        cc = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = ""
        for i in range(8) :
            res = cc[(num & 15)] + res
            num = num >> 4
        return res.lstrip('0')