'''
@author: grekz
'''
class E849_MaximizeDistancetoClosestPerson:

    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i, res, n = 0, 0, len(seats)
        for j, cur in enumerate(seats):
            if cur == 1 :
                if i == 0 : 
                    res = max(res, j - i)
                else :
                    res = max(res, (j - i + 1) // 2)
                i = j + 1
        res = max(res, n - i)
        return res