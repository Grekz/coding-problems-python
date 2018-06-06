'''
@author: grekz
'''
class E530_MinimumAbsoluteDifferenceinBST:

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDiff = 2147483647
        self.prev = None
        def doit(n):
            if not n : return
            doit(n.left)
            if self.prev : self.minDiff = min(self.minDiff, n.val - self.prev.val)
            self.prev = n
            doit(n.right)
        doit(root)
        return self.minDiff