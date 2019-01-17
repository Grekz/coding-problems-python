'''
@author: grekz
'''


class E442_FindAllDuplicatesinanArray:

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            cur = abs(nums[i]) - 1
            if nums[cur] < 0:
                res.append(cur + 1)
            else:
                nums[cur] = -nums[cur]
        return res
