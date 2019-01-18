'''
@author: grekz
'''


class E951_FlipEquivalentBinaryTrees:
    def flipEquiv(self, a, b):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not a or not b:
            return a == b
        return a.val == b.val and (self.flipEquiv(a.left, b.left) and self.flipEquiv(a.right, b.right) or self.flipEquiv(a.left, b.right) and self.flipEquiv(a.right, b.left))
