'''
Created on Mar 9, 2018

@author: grekz
'''

class E226_InvertBinaryTree:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None : return root
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root