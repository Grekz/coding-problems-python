'''
@author: grekz
'''
class E349_IntersectionofTwoArrays:

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 and nums2:
            return list(set(nums1).intersection(nums2))
        return []