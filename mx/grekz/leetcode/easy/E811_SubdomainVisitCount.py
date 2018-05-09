'''
@author: grekz
'''
import collections
class E811_SubdomainVisitCount:

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = collections.defaultdict(int)
        for dom in cpdomains:
            cur = dom.split()
            count = int(cur[0])
            sd = cur[1]
            res[sd] += count
            while( sd.find('.') != -1 ) :
                idx = sd.find('.')
                sd = sd[idx+1:]
                res[sd] += count
        return [str(v) + ' ' + k for k, v in res.items()]