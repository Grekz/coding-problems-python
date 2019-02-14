'''
@author: grekz
'''


class E932_BeautifulArray:

    def beautifulArray(self, N: 'int') -> 'List[int]':
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res if i * 2 - 1 <= N] + \
                [i * 2 for i in res if i * 2 <= N]
        return res
