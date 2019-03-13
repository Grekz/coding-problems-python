'''
@author: grekz
'''
class E985_SumofEvenNumbersAfterQueries:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        cur, res = 0, []
        for x in A :
            cur += x if (x & 1) == 0 else 0
            
        for val, idx in queries:
            if ( (A[idx] & 1) == 0 ) : cur -= A[idx]
            A[idx] += val
            if ( (A[idx] & 1) == 0 ) : cur += A[idx]
            res.append(cur)
            
        return res;