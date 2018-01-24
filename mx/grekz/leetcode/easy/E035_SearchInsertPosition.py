'''
Created on Jan 24, 2018

@author: grekz
'''

class E035_SearchInsertPosition:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        b = len(nums) - 1
        while( a <= b) :
            m = ( a + b ) // 2
            if ( nums[m] == target ) : return m
            if ( nums[m] > target ) :
                b = m - 1
            else:
                a = m + 1
        return a
        