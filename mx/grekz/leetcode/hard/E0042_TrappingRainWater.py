'''
@author: grekz
'''
class E0042_TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        l, r, res, lm, rm = 0, len(height) - 1, 0, 0, 0
        while l < r :
            hl = height[l]
            hr = height[r]
            if hl < hr :
                if hl >= lm :
                    lm = hl
                else:
                    res += lm - hl
                l += 1
            else:
                if hr >= rm :
                    rm =hr
                else:
                    res += rm - hr
                r -= 1
        return res