class E016_3SumClosest:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        le = len(nums) - 1
        for i  in range( 0,  le - 1 ) :
            cur = nums[i]
            if i > 0 and cur == nums[i-1]:
                continue
            l = i + 1 
            h = le
            while l < h :
                tmp = cur + nums[l] + nums[h]
                if tmp == target:
                    return tmp
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp > target:
                    h -= 1
                else:
                    l += 1
        return res
