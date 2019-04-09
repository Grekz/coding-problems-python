'''
@author: grekz
'''
class E1022_SumofRootToLeafBinaryNumbers:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(n, c) :
            if not n :
                return 0
            c = c * 2 + n.val
            if not n.left and not n.right :
                return c
            return dfs(n.left, c) + dfs(n.right, c)
        return dfs(root, 0)