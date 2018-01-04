'''
Created on Jan 4, 2018

@author: grekz
'''

class E018_4Sum:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """        
        res = [] 
        if len(nums) < 4 :
            return res
        nums.sort()
        le = len(nums)
        ma = nums[le - 1]
        maxSum = ma * 3
        for i in range(0, le - 3):
            curr = nums[i];
            if  curr << 2 > target :
                return res
            if  i > 0 and curr == nums[ i - 1 ] :
                continue
            if  curr + maxSum < target :
                continue
            for j in range(i+1, le - 2) :
                if curr + nums[j] * 3 > target : 
                    break
                if j > i +1 and nums[j] == nums[j-1] : 
                    continue
                cc = curr + nums[j]
                l = j + 1
                h = le - 1
                while l < h :
                    tmp = cc + nums[l] + nums[h]
                    if tmp < target :
                        l+=1
                    elif tmp > target :
                        h-=1
                    else:
                        res.append([curr, nums[j], nums[l], nums[h]]);
                        while ( l < h and nums[l] == nums[l+1] ) :
                            l+=1
                        while ( l < h and nums[h] == nums[h-1] ) :
                            h-=1
                        h-=1
                        l+=1
        return res