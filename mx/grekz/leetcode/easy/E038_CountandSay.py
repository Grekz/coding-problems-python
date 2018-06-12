'''
@author: grekz
'''
class E038_CountandSay:

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if ( n < 1 )  : return "0"
        if ( n == 1 ) : return "1"
        if ( n == 2 ) : return "11"
        if ( n == 3 ) : return "21"
        arr = self.countAndSay( n - 1 )
        cur, count = '', 0
        res = ""
        for x in arr:
            if cur != x :
                if count > 0 :
                    res += str(count) + "" + cur
                count = 1
                cur = x
            else:
                count+=1
        res += str(count) + "" + cur
        return res