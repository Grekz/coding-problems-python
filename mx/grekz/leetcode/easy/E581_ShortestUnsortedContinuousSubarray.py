'''
@author: grekz
'''


class E581_ShortestUnsortedContinuousSubarray:

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, ini, end, mi, ma = len(nums), -1, -2, 2147483647, -2147483648
        for i in range(n):
            a = nums[i]
            b = nums[n - 1 - i]
            ma = max(ma, a)
            mi = min(mi, b)
            if a < ma:
                end = i
            if b > mi:
                ini = n - 1 - i
        return end - ini + 1
