'''
@author: grekz
'''
class E1026_MaximumDifferenceBetweenNodeandAncestor:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs( node, ma, mi ) :
            if not node :
                return ma - mi
            ma = max(ma, node.val)
            mi = min(mi, node.val)
            maxLeft = dfs(node.left, ma, mi)
            maxRight = dfs(node.right, ma, mi)
            return max(maxLeft, maxRight)
        return dfs(root, root.val, root.val)