'''
@author: grekz
'''
class E345_ReverseVowelsofaString:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 : return s
        vows = "aeiouAEIOU"
        i = 0
        j = len(s) - 1
        st = list(s)
        while i < j:
            while i < j and st[i] not in vows : i+=1
            while i < j and st[j] not in vows : j-=1
            if i < j : st[j], st[i] = st[i], st[j]
            i+=1
            j-=1
        return "".join(st)
        