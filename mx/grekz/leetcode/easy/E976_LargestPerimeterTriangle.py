'''
@author: grekz
'''


class E976_LargestPerimeterTriangle:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        for i in range(len(A) - 1, 1, -1):
            if A[i] < (A[i-1] + A[i-2]):
                return A[i] + A[i-1] + A[i-2]
        return 0
