'''
@author: grekz
'''
class E486_PredicttheWinner:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                a = nums[i] - dp[j]
                b = nums[j] - dp[j - 1]
                dp[j] = max(a, b)
                
        return dp[n - 1] >= 0