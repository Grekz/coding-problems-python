'''
@author: grekz
'''
class E448_FindAllNumbersDisappearedinanArray:

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            v = abs(x) - 1
            nums[ v ] = -abs(nums[ v ])
        return [ i + 1 for i, x in enumerate(nums) if x > 0]