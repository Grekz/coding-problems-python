'''
@author: grekz
'''


class E031_NextPermutation:

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        i, j = n - 1, n
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        while i < n:
            nums[i], nums[n] = nums[n], nums[i]
            i += 1
            n -= 1
