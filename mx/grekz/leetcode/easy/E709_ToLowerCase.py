'''
@author: grekz
'''
class E709_ToLowerCase:

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """        
        res = ""
        for c in str:
            oc = ord(c)
            res += chr(oc + 32) if 90 >= oc >= 65 else c 
        return res
        