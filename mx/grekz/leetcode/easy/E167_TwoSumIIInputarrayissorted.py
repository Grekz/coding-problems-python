'''
Created on Feb 15, 2018

@author: grekz
'''

class E167_TwoSumIIInputarrayissorted:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = len(numbers) - 1 
        i = 0
        while(i < j) :
            sum = numbers[j] + numbers[i]
            if (sum < target): i+=1
            elif(sum > target): j-=1
            else: return [i+1,j+1]
        return [-1,-1]
        