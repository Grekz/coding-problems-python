'''
@author: grekz
'''


class E365_WaterandJugProblem:

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            if (b == 0):
                return a
            return gcd(b, a % b)
        if (x + y < z):
            return False
        if (x == z or y == z or x + y == z):
            return True
        return z % gcd(x, y) == 0
