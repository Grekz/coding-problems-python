'''
@author: grekz
'''
class E836_RectangleOverlap:

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])        