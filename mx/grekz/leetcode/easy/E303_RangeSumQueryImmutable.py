'''
@author: grekz
'''
# class E303_RangeSumQueryImmutable:
class NumArray(object):
    numsCache = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if (nums == None or len(nums) < 1): return
        self.numsCache = nums
        cur = nums[0]
        for i in range(1, len(nums)):
            self.numsCache[i] = nums[i] + self.numsCache[ i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (self.numsCache == None or len(self.numsCache) < 1 ) : return 0
        return self.numsCache[j] - (0 if i == 0 else self.numsCache[i-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)