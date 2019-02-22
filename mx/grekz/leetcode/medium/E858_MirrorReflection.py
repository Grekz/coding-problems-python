'''
@author: grekz
'''


class E858_MirrorReflection:
    def mirrorReflection(self, p: 'int', q: 'int') -> 'int':
        def gcd(a, b):
            if (a == 0):
                return b
            return gcd(b % a, a)
        g = gcd(p, q)
        p //= g
        p %= 2
        q //= g
        q %= 2
        if p == 1 and q == 1:
            return 1
        if p == 1:
            return 0
        return 2
