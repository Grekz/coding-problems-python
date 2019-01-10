'''
@author: grekz
'''


class E704_BinarySearch:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bSearch(nums, target, 0, len(nums) - 1)

    def bSearch(self, nums, target, ini, end):
        if ini > end:
            return -1
        mid = ini + (end - ini) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.bSearch(nums, target, ini, mid - 1)
        return self.bSearch(nums, target, mid + 1, end)
