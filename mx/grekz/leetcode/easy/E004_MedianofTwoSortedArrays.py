'''
Created on Dec 3, 2017

@author: grekz
'''
import sys

class E004_MedianofTwoSortedArrays:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        h = a = len(nums1)
        b = len(nums2)
        if a > b :
            return self.findMedianSortedArrays(nums2, nums1)
        l = 0
        while l <= h :
            m1 = int(( l + h ) / 2)
            m2 = int(( a + b + 1) / 2 - m1)
            mla = nums1[m1 - 1] if m1 != 0 else -sys.maxsize - 1
            mlb = nums2[m2 - 1] if m2 != 0 else -sys.maxsize - 1
            mra = nums1[m1] if m1 != a else sys.maxsize
            mrb = nums2[m2] if m2 != b else sys.maxsize
            if mla > mrb:
                h = m1 - 1
            elif mlb > mra:
                l = m1 + 1
            else:
                return float(max( mla, mlb )) if ( a + b ) % 2 != 0 else ( max(mla, mlb) + min(mra ,mrb) ) / 2
        return -1.0