'''
@author: grekz
'''
class E0135_Candy:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        tmp = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1] :
                tmp[i] = tmp[i - 1] + 1
        res = tmp[n - 1]
        for i in range( n-2, -1, -1):
            if ratings[i] > ratings[i+1] :
                tmp[i] = max(tmp[i], tmp[i+1] + 1)
            res += tmp[i]
        return res