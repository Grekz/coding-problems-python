'''
@author: grekz
'''
class E128_LongestConsecutiveSequence:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, res = set(nums), 0
        for x in nums :
            if not x - 1 in s :
                y = x + 1
                while y in s:
                    y += 1
                res = max(res, y - x)
        return res