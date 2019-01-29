'''
@author: grekz
'''


class E055_JumpGame:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums) - 1
        for i in range(last, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0
