'''
@author: grekz
'''
class E0394_DecodeString:
    def decodeString(self, s: str) -> str:
        n, stack, res, i = len(s), [], "", 0
        while i < n:
            c = s[i]
            if c.isdigit() :
                tmpDig = ""
                while c.isdigit() :
                    i += 1
                    tmpDig += c
                    c = s[i]
                stack.append(res)
                stack.append(tmpDig)
                res = ""
            elif c == ']' :
                tmpRes = ""
                for j in range(int(stack.pop())) :
                    tmpRes += res
                res = stack.pop() + tmpRes
            else :
                res += c
            i += 1
        return res