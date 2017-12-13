'''
Created on Dec 13, 2017

@author: grekz
'''
class E014_LongestCommonPrefix:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """        
        if len(strs) < 1 :
            return ""
        prefix = strs.pop(0)
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[0:-1]
        return prefix;