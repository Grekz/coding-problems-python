'''
@author: grekz
'''
class E496_NextGreaterElementI:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        s = []
        for x in nums2:
            while s and s[-1] < x:
                m[s.pop()] = x
            s.append(x)
        for i in range(len(nums1)):
            nums1[i] = m.get(nums1[i], -1)
        return nums1