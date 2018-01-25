'''
Created on Jan 25, 2018

@author: grekz
'''

class E053_MaximumSubarray:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = res = nums[0]
        for i in range( 1, len(nums)) :
            cur = max(cur+nums[i], nums[i])
            res = max(cur,res)
        return res
        