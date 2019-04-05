'''
@author: grekz
'''
class E0941_ValidMountainArray:
    def validMountainArray(self, A: List[int]) -> bool:
        n, i = len(A), 0
        while ( i + 1 < n and A[i] < A[i + 1] ) : i+=1  
        if ( i== 0 or i == n - 1 ) : return False
        while ( i + 1 < n and A[i] > A[i + 1] ) : i+=1
        return i == n - 1