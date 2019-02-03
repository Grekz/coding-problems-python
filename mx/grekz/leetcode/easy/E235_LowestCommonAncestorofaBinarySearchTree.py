'''
@author: grekz
'''


class E235_LowestCommonAncestorofaBinarySearchTree:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
