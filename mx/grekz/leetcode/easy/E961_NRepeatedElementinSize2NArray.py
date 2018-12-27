'''
@author: grekz
'''
class E961_NRepeatedElementinSize2NArray:

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        c = {}
        for x in A:
            if x in c:
                return x
            c[x] = 1
        return -1