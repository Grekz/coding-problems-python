'''
@author: grekz
'''
class E443_StringCompression:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        indAns = ind = 0
        n = len(chars)
        while ( ind < n ) :
            c = chars[ind]
            cc = 0
            while ( ind < n and c == chars[ind] ) :
                cc += 1
                ind += 1
            chars[indAns] = c
            indAns += 1
            if ( cc > 1 ) :
                for x in str(cc) :
                    chars[indAns] = x
                    indAns += 1
        return indAns