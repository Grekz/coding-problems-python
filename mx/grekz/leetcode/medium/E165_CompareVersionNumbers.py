'''
@author: grekz
'''


class E165_CompareVersionNumbers:

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a, b = version1.split("."), version2.split(".")
        al, bl = len(a), len(b)
        n = max(al, bl)
        for i in range(n):
            c = (int(a[i]) if i < al else 0) - (int(b[i]) if i < bl else 0)
            if c > 0:
                return 1
            elif c < 0:
                return -1
        return 0
