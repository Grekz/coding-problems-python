'''
@author: grekz
'''


class E789_EscapeTheGhosts:

    def escapeGhosts(self, ghosts: 'List[List[int]]', target: 'List[int]') -> 'bool':
        t0, t1 = target[0], target[1]
        dest = abs(t0) + abs(t1)
        for g in ghosts:
            cur = abs(g[1]-t1) + abs(g[0]-t0)
            if cur <= dest:
                return False
        return True
