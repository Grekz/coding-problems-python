'''
@author: grekz
'''
class E824_GoatLatin:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = "aeiouAEIOU"
        res = ""
        i = 1
        for c in S.split() :
            res += " "
            curChar = c[0]
            if curChar in vowels :
                res += c
            else:
                res += c[1:] + curChar 
            
            res += "ma"
            for _ in range(i) :
                res += "a"
            i += 1
        return res[1:]