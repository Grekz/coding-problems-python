'''
@author: grekz
'''
class E1010_PairsofSongsWithTotalDurationsDivisibleby60:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, cnt = 0, [0] * 60
        for x in time :
            d = (60 - x % 60) % 60
            res += cnt[d]
            cnt[x % 60] += 1
        return res