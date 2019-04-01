'''
@author: grekz
'''
class E1013_PartitionArrayIntoThreePartsWithEqualSum:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s //= 3
        cnt, tmp = 0, 0
        for x in A :
            tmp += x
            if tmp == s :
                cnt += 1
                tmp = 0
        return cnt == 3