'''
@author: grekz
'''
class E287_FindtheDuplicateNumber:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2 :
            return -1
        for i in range(n):
            cur = abs(nums[i]) - 1
            if nums[cur] < 0 :
                return cur + 1
            nums[cur] = -nums[cur]
        return -1