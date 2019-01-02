'''
@author: grekz
'''


class E942_DIStringMatch:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        left, right, res = 0, n, []
        for x in S:
            cur = left
            if x == "I":
                left += 1
            else:
                cur = right
                right -= 1
            res.append(cur)
        res.append(right)
        return res
