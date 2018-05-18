'''
@author: grekz
'''
class E543_DiameterofBinaryTree:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def doit(n):
            if not n : return 0
            le, ri = doit(n.left), doit(n.right)
            self.res = max(self.res, le + ri)
            return 1 + max(le, ri)
        doit(root)
        return self.res