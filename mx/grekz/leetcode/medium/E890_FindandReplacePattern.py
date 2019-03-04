'''
@author: grekz
'''
class E890_FindandReplacePattern:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(a):
            di = {}
            i = 0
            for y in a:
                pi = pattern[i]
                if not y in di:
                    di[y] = pi
                if di[y] != pi:
                    return False
                i += 1
            ch = [False] * 26
            for z in di.values():
                if ch[ord(z) - 97] :
                    return False
                ch[ord(z) - 97] = True
            return True
            
        res = []
        for x in words:
            if check(x) :
                res.append(x)
        return res