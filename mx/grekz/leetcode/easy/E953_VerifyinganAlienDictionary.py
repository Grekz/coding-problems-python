'''
@author: grekz
@url http://grekz.wordpress.com
'''
class E953_VerifyinganAlienDictionary:

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) < 2 :
            return True
        dic = self.createDict(order)
        prev = words[0]
        for w in words:
            if self.compare(prev, w, dic) > 0:
                return False
            prev = w
        return True
    
    def createDict(self, s):
        return { char: index for index, char in enumerate(s) }
    
    def compare(self, a, b, dic):
        al, bl, com, i = len(a), len(b), 0, 0
        while i < al and i < bl and com == 0:
            com = dic[a[i]] - dic[b[i]]
            i+=1
        return al - bl if com == 0 else com