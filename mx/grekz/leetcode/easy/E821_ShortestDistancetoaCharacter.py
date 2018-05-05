'''
@author: grekz
'''
class E821_ShortestDistancetoaCharacter:

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        n = len(S)
        res = [0] * n
        pos = -n
        for i, x in enumerate(S) :
            if C == x :
                pos = i
            else:
                res[i] = i - pos
        for i in range(n-1, -1, -1):
            x = S[i]
            if C == x :
                pos = i
            else:
                res[i] = min(res[i], abs(i - pos))
        return res