'''
@author: grekz
'''


class E338_CountingBits:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n = num + 1
        res = [0] * n
        for i in range(1, n):
            res[i] = res[i//2] + i % 2
        return res
