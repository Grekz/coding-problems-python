'''
@author: grekz
'''
class E434_NumberofSegmentsinaString:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
