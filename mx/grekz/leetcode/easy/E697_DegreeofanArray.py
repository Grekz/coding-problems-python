'''
@author: grekz
'''


class E697_DegreeofanArray:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts, ini, res, ma = {}, {}, len(nums), 0
        for i, x in enumerate(nums):
            curIni = ini.get(x, i)
            cur = counts.get(x, 0) + 1
            counts[x] = cur
            ini[x] = curIni
            if ma < cur:
                ma = cur
                res = i - curIni + 1
            elif ma == cur:
                res = min(res, i - curIni + 1)
        return res
