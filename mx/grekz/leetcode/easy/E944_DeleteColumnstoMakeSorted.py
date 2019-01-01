'''
@author: grekz
'''
class E944_DeleteColumnstoMakeSorted:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        lenA = len(A)
        lenW = len(A[0])
        res = 0
        for i in range(lenW):
            for j in range(lenA-1):
                if A[j][i] > A[j+1][i]:
                    res+=1
                    break
        return res