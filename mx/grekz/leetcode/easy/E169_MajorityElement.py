'''
Created on Feb 17, 2018

@author: grekz
'''

class E169_MajorityElement:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 : return -1
        if len(nums) < 3 : return nums[0]
        count = res = 0
        for x in nums:
            if count == 0 : res = x
            if x == res : count += 1
            else: count -= 1
        return res
        