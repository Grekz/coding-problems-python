'''
@author: grekz
'''
class E665_NondecreasingArray:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        exists = False
        for i in range(1, n) :
            if nums[i] < nums[i-1] :
                if exists :
                    return False
                exists = True
                if i > 1 and nums[i] < nums[i-2] :
                    nums[i] = nums[i-1]
        return True