'''
@author: grekz
'''
class E080_RemoveDuplicatesfromSortedArrayII:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 3 : 
            return len(nums)
        i = 0
        for n in nums :
            if i < 2 or nums[ i - 2 ] < n :
                nums[i] = n
                i += 1
        return i