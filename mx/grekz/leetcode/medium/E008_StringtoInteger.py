'''
Created on Dec 24, 2017

@author: grekz
'''
class E008_StringtoInteger:
    def myAtoi(self, str):
        """
        :type str: str1
        :rtype: int
        """
        str = str.strip()
        if len(str) < 1 :
            return 0
        z = '0'
        n = '9'
        sign = res = ''
        if str[0] == '-' or str[0] == '+' :
            sign = str[0]
            str = str[1::]
        for x in str :
            if x >= z and x <= n :
                res += x
            else:
                break
        if res != '' :
            resInt = int( sign + res )
            if  resInt > 2147483647 : return 2147483647
            if  resInt < -2147483648 : return -2147483648
            return resInt        
        return 0
            