'''
@author: grekz
'''
import collections
class E350_IntersectionofTwoArraysII:

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 and nums2:
            a,b = map(collections.Counter, (nums1,nums2))
            return list((a&b).elements())
        return []