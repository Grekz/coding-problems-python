'''
@author: grekz
'''
import collections
class E454_4SumII:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m = collections.Counter( a+b for a in A for b in B )
        return sum( m[-(a+b)] for a in C for b in D )