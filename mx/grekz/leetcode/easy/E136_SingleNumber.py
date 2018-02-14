'''
Created on Feb 14, 2018

@author: grekz
'''
import functools

class E136_SingleNumber:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(lambda x,y: x^y, nums)
        