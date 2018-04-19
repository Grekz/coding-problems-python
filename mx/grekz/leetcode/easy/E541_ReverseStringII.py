'''
@author: grekz
'''
class E541_ReverseStringII:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        cArr = list(s)
        n = len(cArr)
        for i in range(0,n, 2 * k):
            ii = i 
            j = n - 1 if i + k - 1 > n - 1 else i + k - 1
            while ii < j :
                tmp = cArr[ii]
                cArr[ii] = cArr[j]
                ii+=1
                cArr[j] = tmp
                j-=1 
        return "".join(cArr)