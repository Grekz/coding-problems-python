'''
@author: grekz
'''
class E791_CustomSortString:

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = [0] * 26
        res = ""
        for x in T:
            t[ord(x) - 97] += 1
        for x in S:
            while t[ord(x) - 97] > 0 :
                res += x
                t[ord(x) - 97] -= 1
        for x in T:
            while t[ord(x) - 97] > 0:
                t[ord(x) - 97] -= 1
                res += x
        return res