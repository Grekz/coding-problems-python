'''
@author: grekz
'''
class E765_CouplesHoldingHands:
    def minSwapsCouples(self, row: List[int]) -> int:
        n, res = len(row), 0
        pos = [0] * n
        for i in range(n):
            pos[row[i]] = i
        for i in range(0, n, 2):
            pair = row[i] ^ 1
            if pair != row[i+1] :
                row[pos[pair]] = row[i+1]
                pos[row[i+1]] = pos[pair]
                res += 1
        return res