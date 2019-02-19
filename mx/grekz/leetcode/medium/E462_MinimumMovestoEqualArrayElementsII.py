'''
@author: grekz
'''


class E462_MinimumMovestoEqualArrayElementsII:

    def minMoves2(self, nums: 'List[int]') -> 'int':
        nums.sort()
        i, res, j = 0, 0, len(nums) - 1
        while i < j:
            res += nums[j] - nums[i]
            j -= 1
            i += 1
        return res
