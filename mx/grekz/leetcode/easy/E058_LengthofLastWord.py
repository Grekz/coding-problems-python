'''
Created on Jan 26, 2018

@author: grekz
'''

class E058_LengthofLastWord:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        return len(s) - s.rfind(' ') - 1
        