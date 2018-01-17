'''
Created on Jan 17, 2018

@author: grekz
'''

class E026_RemoveDuplicatesfromSortedArray:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if ( len(nums) < 1 ) : return 0
        if ( len(nums) == 1 ) : return 1
        le = len(nums) 
        base = nums[0]
        count = 0
        cur = 1
        for i in range(1,le) :
            if ( base == nums[i] ) :
                count += 1
                nums[i] = -1
            else:
                base = nums[i]
                nums[cur] = nums[i]
                cur += 1
        return le - count      