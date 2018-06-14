'''
@author: grekz
'''
class E098_ValidateBinarySearchTree:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return root == None or self.dfs(root, 2147483648, -2147483649)
    
    def dfs(self, root, max, min):
        return root == None or \
        not (root.val >= max or root.val <= min) and \
        self.dfs(root.left, root.val, min) and \
        self.dfs(root.right, max, root.val)