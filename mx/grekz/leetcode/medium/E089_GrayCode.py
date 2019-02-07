'''
@author: grekz
'''


class E089_GrayCode:
    def grayCode(self, n: 'int') -> 'List[int]':
        return [i ^ i >> 1 for i in range(2**n)]
