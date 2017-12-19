'''
Created on Dec 19, 2017

@author: grekz
'''
class E017_LetterCombinationsofaPhoneNumber:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0 or "0" in digits or "1" in digits :
            return []
        res = ['']
        cArr = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"
        }
        for x in digits:
            tmp = []
            for y in cArr[x] :
                for r in res :
                    tmp.append( r + y )
            res = tmp
        return res