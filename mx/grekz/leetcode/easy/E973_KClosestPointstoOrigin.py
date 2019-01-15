'''
@author: grekz
'''


class E973_KClosestPointstoOrigin:

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])[:K]
