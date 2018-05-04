'''
@author: grekz
'''
class E598_RangeAdditionII:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a, b = m, n
        for x in ops :
            a = min(a, x[0])
            b = min(b, x[1])
        return a * b