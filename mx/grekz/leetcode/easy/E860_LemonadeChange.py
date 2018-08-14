'''
@author: grekz
'''
class E860_LemonadeChange:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        f = t = 0
        for x in bills:
            if x == 5 :
                f += 1
            elif x == 10:
                f -= 1
                t += 1
            elif t > 0:
                t -= 1
                f -= 1
            else:
                f -= 3
            if f < 0 or t < 0:
                return False
        return True
        