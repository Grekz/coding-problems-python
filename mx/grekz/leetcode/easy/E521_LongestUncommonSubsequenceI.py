'''
@author: grekz
'''
class E521_LongestUncommonSubsequenceI:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b :
            return -1
        return max(len(a), len(b))
        