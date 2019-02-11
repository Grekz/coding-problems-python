'''
@author: grekz
'''


class E393_UTF8Validation:

    def validUtf8(self, data: 'List[int]') -> 'bool':
        c = 0
        for d in data:
            if (d >= 128 and d <= 191):
                if (c == 0):
                    return False
                c -= 1
            else:
                if (c != 0):
                    return False
                if (d >= 128):
                    if (d < 224):
                        c = 1
                    elif (d < 240):
                        c = 2
                    elif (d < 248):
                        c = 3
                    else:
                        return False
        return c == 0
