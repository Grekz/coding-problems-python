'''
Created on Feb 22, 2018

@author: grekz
'''

class E189_RotateArray:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n == 0 or k == 0: return
        def reverse( nums, i, j ):
            while( i < j):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1; j -=1
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        
        