'''
@author: grekz
'''


class E739_DailyTemperatures:

    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        n, top = len(T), -1
        res, stack = [0] * n, [0] * n
        for i in range(n):
            while top >= 0 and T[i] > T[stack[top]]:
                idx = stack[top]
                res[idx] = i - idx
                top -= 1
            top += 1
            stack[top] = i
        return res
