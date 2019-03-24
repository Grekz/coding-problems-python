'''
@author: grekz
'''
class E0300_LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if ( n < 1 ) :
            return 0
        dp, res =[0] * n, 1
        dp[0] = 1
        for i in range(1, n) :
            val = 0
            for j in range(i) :
                if ( nums[i] > nums[j] ) :
                    val = max(val, dp[j])
            dp[i] = val + 1
            res = max(res, dp[i])
        return res