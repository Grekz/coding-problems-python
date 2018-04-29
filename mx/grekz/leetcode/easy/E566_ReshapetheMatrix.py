'''
@author: grekz
'''
class E566_ReshapetheMatrix:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        if n * m != r * c :
            return nums
        res = [ [ None for i in range(c) ] for j in range(r) ]
        i = 0
        for curArr in nums :
            for cur in curArr :
                cc = i%c
                ic = i//c
                res[ic][cc] = int(cur)
                i += 1
        return res