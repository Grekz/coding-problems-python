'''
@author: grekz
'''
class E830_PositionsofLargeGroups:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S += '|'
        res = []
        ps = 0
        for i in range(len(S)) :
            if S[i] != S[ps] :
                if i - ps > 2 :
                    res += [[ps, i-1]]
                ps = i
        return res