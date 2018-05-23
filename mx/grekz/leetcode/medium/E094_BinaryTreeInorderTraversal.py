'''
@author: grekz
'''
class E094_BinaryTreeInorderTraversal:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def doit(n) :
            if n :
                doit(n.left)
                self.res += [n.val]
                doit(n.right)
        doit(root)
        return self.res