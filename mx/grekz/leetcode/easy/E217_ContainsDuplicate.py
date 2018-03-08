'''
Created on Mar 8, 2018

@author: grekz
'''

class E217_ContainsDuplicate:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        