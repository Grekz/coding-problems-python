'''
Created on Jan 18, 2018

@author: grekz
'''

class E027_RemoveElement:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)) :
            if ( nums[i] != val ) :
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1
        return count
        