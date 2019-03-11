'''
@author: grekz
'''
class E979_DistributeCoinsinBinaryTree:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(n) :
            if not n : return 0
            l, r = dfs(n.left), dfs(n.right)
            self.ans += abs(l) + abs(r)
            return n.val + l + r - 1
        dfs(root)
        return self.ans