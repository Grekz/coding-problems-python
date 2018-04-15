'''
@author: grekz
'''
class E482_LicenseKeyFormatting:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cArr = S.upper().replace("-","")
        res = ""
        le = len(cArr)
        s1 = K if le%K==0 else le%K
        res = cArr[:s1]
        while le > s1 :
            res += '-' + cArr[s1:s1+K]
            s1 += K
        return res