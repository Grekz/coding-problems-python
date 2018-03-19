'''
@author: grekz
'''
class E268_MissingNumber:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i, e in enumerate(nums):
            res ^= i ^ e
        return res ^ len(nums)