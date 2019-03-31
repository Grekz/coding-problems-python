'''
@author: grekz
'''
class E1018_BinaryPrefixDivisibleBy5:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        tmp, res = 0, []
        for x in A :
            tmp = ( (tmp << 1) + x ) % 5
            res.append(tmp == 0)
        return res