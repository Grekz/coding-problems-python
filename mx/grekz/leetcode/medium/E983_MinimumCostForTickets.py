'''
@author: grekz
'''


class E983_MinimumCostForTickets:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def goz(a, b):
            if a < b:
                return 0
            return a - b
        mint, n = 2147483647, days[-1] + 1
        cd = [0] * n
        for x in days:
            cd[x] = mint
        for i in range(1, n):
            if cd[i] == mint:
                mc = cd[i - 1] + costs[0]
                mc = min(mc, cd[goz(i, 7)] + costs[1])
                mc = min(mc, cd[goz(i, 30)] + costs[2])
                cd[i] = mc
            else:
                cd[i] = cd[i - 1]
        return cd[n-1]
