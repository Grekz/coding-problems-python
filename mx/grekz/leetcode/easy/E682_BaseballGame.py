'''
@author: grekz
'''
class E682_BaseballGame:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res, val = 0, 0
        rounds = []
        for s in ops :
            last = len(rounds) - 1
            if(s == "C") :
                val = -rounds[last]
                rounds.pop(last)
            else:
                if s == "+" :
                    val = rounds[last] + rounds[last-1]
                elif s == "D" :
                    val = 2 * rounds[last]
                else:
                    val = int(s)
                rounds += [val]
            res += val
        return res