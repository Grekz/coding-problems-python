'''
Created on Dec 4, 2017
https://leetcode.com/problems/longest-palindromic-substring/description/
@author: grekz
'''
class E005_LongestPalindromicSubstring:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = ['$','#']
        for c in s: t.extend([c,'#'])
        t.extend('%')
        c = r = mC = mP = 0
        lt = len(t)
        p = [0] * lt
        for i in range(1,lt-1) :
            if i < r :
                mir = 2*c - i
                p[i] = min(r - i, p[mir])
            while t[i - (1 + p[i])] == t[i + (1 + p[i])]: p[i]+=1
            if i + p[i] > r :
                c = i
                r = i + p[i]
                if mP < p[i]:
                    mP = p[i]
                    mC = i
        st = (mC - mP) // 2
        en = (mC + mP) // 2
        return s[st:en]