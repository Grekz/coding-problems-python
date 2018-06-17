'''
@author: grekz
'''
class E852_PeakIndexinaMountainArray:

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, m = 0, -2147483648
        for i, x in enumerate(A) :
            if x > m :
                res = i
                m = x
        return res