'''
Created on Mar 1, 2018

@author: grekz
'''

class E198_HouseRobber:
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in range(0,len(nums)):
            if i % 2 == 0:
                a = max(nums[i] + a, b)
            else:
                b = max(a, b + nums[i])
        return max(a,b)