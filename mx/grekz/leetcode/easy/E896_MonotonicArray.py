'''
@author: grekz
'''


class E896_MonotonicArray:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a, b = True, True
        for i in range(1, len(A)):
            a = a and A[i-1] <= A[i]
            b = b and A[i-1] >= A[i]
        return a or b
