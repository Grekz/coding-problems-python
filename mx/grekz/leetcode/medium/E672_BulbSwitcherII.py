'''
@author: grekz
'''


class E672_BulbSwitcherII:
    def flipLights(self, n: 'int', m: 'int') -> 'int':
        if(m == 0):
            return 1
        if(n == 1):
            return 2
        if(n == 2 and m == 1):
            return 3
        if(n == 2):
            return 4
        if(m == 1):
            return 4
        if(m == 2):
            return 7
        return 8
