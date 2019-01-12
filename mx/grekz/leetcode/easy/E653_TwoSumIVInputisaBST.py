'''
@author: grekz
'''


class E653_TwoSumIVInputisaBST:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        return self.dfs(root, k, s)

    def dfs(self, node, k, s):
        if not node:
            return False
        if k - node.val in s:
            return True
        s.add(node.val)
        return self.dfs(node.left, k, s) or self.dfs(node.right, k, s)
