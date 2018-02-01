'''
Created on Feb 1, 2018

@author: grekz
'''

class E088_MergeSortedArray:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if ( n == 0 ) :
             return
        i = m -1 
        j = n - 1
        ind = n + m  - 1
        while(ind >= 0 ) :
            if(i < 0) : 
                nums1[ind] = nums2[j]
                j -= 1
            elif(j < 0): 
                nums1[ind] = nums1[i]
                i-=1
            elif(nums1[i] > nums2[j]): 
                nums1[ind] = nums1[i]
                i-=1
            else: 
                nums1[ind] = nums2[j]
                j-=1
            ind -=1