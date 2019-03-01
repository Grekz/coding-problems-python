'''
@author: grekz
'''
class E228_SummaryRanges:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n, i, res = len(nums), 0, []
        while i < n :
            c = str(nums[i])
            while i + 1 < n and nums[i + 1] - nums[i] == 1 :
                i += 1
            d = str(nums[i])
            res.append( c + ( "" if c == d else "->" + d ) )
            i += 1
        return res