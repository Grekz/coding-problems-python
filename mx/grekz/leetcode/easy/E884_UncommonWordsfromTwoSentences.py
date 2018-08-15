'''
@author: grekz
'''
class E884_UncommonWordsfromTwoSentences:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = collections.Counter( ( A + " " + B ).split() )
        return [ e for e, c in c.items() if c == 1 ]