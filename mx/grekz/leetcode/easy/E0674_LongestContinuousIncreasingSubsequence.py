'''
@author: grekz
'''
class E0674_LongestContinuousIncreasingSubsequence:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res, count, n = 0, 0, len(nums)
        for i in range(n):
            if i < 1 or nums[i-1] < nums[i] :
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res