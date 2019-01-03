'''
@author: grekz
'''


class E922_SortArrayByParityII:
    def sortArrayByParityII(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, res = 0, 1, [0] * len(a)
        for x in a:
            if x & 1 == 0:
                res[i] = x
                i += 2
            else:
                res[j] = x
                j += 2
        return res
