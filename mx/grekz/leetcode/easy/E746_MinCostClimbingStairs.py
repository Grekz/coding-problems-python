'''
@author: grekz
'''


class E746_MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
