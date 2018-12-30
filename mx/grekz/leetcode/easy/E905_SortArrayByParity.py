'''
@author: grekz
'''
class E905_SortArrayByParity:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j :
            cur = A[i]
            if cur % 2 == 1 :
                A[i] = A[j]
                A[j] = cur
                j -= 1
            else:
                i += 1
        return A