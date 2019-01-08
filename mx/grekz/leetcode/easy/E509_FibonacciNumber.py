'''
@author: grekz
'''


class E509_FibonacciNumber:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return N if N < 2 else self.fib(N-1) + self.fib(N-2)
