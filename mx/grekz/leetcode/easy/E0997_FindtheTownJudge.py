'''
@author: grekz
'''
class E0997_FindtheTownJudge:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        c = [0] * (N + 1)
        for x in trust :
            c[x[0]] -= 1
            c[x[1]] += 1
        for i in range( 1, N + 1 ) :
            if ( c[i] == N - 1 ) :
                return i
        return -1