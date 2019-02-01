'''
@author: grekz
'''


class E982_TripleswithBitwiseANDEqualToZero:

    def countTriplets(self, A: 'List[int]') -> 'int':
        res, tmp = 0, collections.defaultdict(int)
        for a in A:
            for b in A:
                tmp[a & b] += 1
        for k, v in tmp.items():
            for b in A:
                if (k & b) == 0:
                    res += v
        return res
