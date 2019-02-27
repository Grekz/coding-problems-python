'''
@author: grekz
'''
class E322_CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m, n = amount + 1, len(coins)
        dp = [m] * m
        dp[0] = 0
        for i in range(1,m):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
                    
        if dp[amount] <= amount:
            return dp[amount]
        return -1