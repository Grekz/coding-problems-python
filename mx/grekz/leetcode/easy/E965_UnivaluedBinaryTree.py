'''
@author: grekz
'''
class E965_UnivaluedBinaryTree:

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root :
            if root.left and \
            root.left.val != root.val or \
            not self.isUnivalTree(root.left):
                return False
            if root.right and \
            root.right.val != root.val or \
            not self.isUnivalTree(root.right):
                return False
        return True