'''
@author: grekz
'''
class E832_FlippinganImage:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(lambda x : list(map(lambda y : y ^ 1, x[::-1])), A))