'''
@author: grekz
'''


class E872_LeafSimilarTrees:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(n): return "" if not n else dfs(n.left) + \
            dfs(n.right) + (str(n.val) if n.left == n.right else "")
        return dfs(root1) == dfs(root2)
