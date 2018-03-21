'''
@author: grekz
'''
class E290_WordPattern:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(words) != len(pattern) :
            return False
        dic = {}
        for i, x in enumerate(words):
            char = pattern[i]
            if char in dic:
                if dic[char] != x : return False
            elif x in dic.values():
                return False
            else:
                dic[char] = x
        return True