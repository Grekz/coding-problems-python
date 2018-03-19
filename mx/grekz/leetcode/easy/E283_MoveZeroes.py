'''
@author: grekz
'''
class E283_MoveZeroes:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i, e in enumerate(nums):
            if(e != 0):
                tmp = e
                nums[i] = nums[pointer]
                nums[pointer] = tmp
                pointer += 1