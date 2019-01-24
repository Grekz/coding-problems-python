'''
@author: grekz
'''


class E034_FindFirstandLastPositionofElementinSortedArray:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums or not len(nums):
            return [-1, -1]
        idx = self.bSearch(nums, target, True)
        if (nums[idx % len(nums)] != target):
            return [-1, -1]
        rIdx = self.bSearch(nums, target, False) - 1
        return [idx, rIdx]

    def bSearch(self, n, t, left):
        a, b, m = 0, len(n), 0
        while a < b:
            m = a + (b - a) // 2
            if n[m] > t or (left and n[m] == t):
                b = m
            else:
                a = m + 1
        return a
