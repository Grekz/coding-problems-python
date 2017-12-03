'''
Created on Dec 3, 2017
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

@author: grekz
'''
class E003_LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = prev = i = 0
        dic = {}
        for x in s:
            if x in dic and dic[x] >= prev:
                res = max( i - prev, res )
                prev = dic[x] + 1
            dic[x] = i
            i += 1
            
        return max( i - prev, res )
        