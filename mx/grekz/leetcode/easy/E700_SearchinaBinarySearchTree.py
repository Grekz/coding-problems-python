'''
@author: grekz
'''


class E700_SearchinaBinarySearchTree:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)
