'''
Created on Jan 18, 2018

@author: grekz
'''

class E028_ImplementstrStr:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def str_str_helper(haystack, needle, idx):
            nLen = len(needle)
            if ( len(haystack)-idx < nLen ): return -1 
            if ( haystack[idx:(idx+nLen)] == needle ) : return idx 
            return str_str_helper(haystack, needle, idx+1)
        return str_str_helper(haystack,needle,0)