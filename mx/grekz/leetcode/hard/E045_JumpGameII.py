'''
@author: grekz
'''


class E045_JumpGameII:
    def jump(self, nums: 'List[int]') -> 'int':
        count, end, far, n = 0, 0, 0, len(nums) - 1
        for i in range(n):
            far = max(far, i + nums[i])
            if i == end:
                count += 1
                end = far
        return count
