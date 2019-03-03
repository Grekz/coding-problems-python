'''
@author: grekz
'''
class E779_KthSymbolinGrammar:
    def kthGrammar(self, N: int, K: int) -> int:
        n, k = 0, K - 1
        while k > 0 :
            k &= k - 1
            n += 1
        return n & 1