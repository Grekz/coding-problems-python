'''
@author: grekz
'''
class E814_BinaryTreePruning:

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root :
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)        
        if not root.left and not root.right and root.val == 0:
            root = None
        return root