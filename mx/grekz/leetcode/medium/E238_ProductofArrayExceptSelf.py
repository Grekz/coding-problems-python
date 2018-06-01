'''
@author: grekz
'''
class E238_ProductofArrayExceptSelf:

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = 1
        n = len(nums)
        p = [1] * n
        for i, e in enumerate(nums) :
            p[i] = t
            t *= e
        t = 1
        for i, e in enumerate(nums[::-1]):
            p[ n - i - 1 ] *= t
            t *= e
        return p