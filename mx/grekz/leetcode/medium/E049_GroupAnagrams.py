'''
@author: grekz
'''
class E049_GroupAnagrams:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs :
            key = str(sorted(s))
            m[key] = m.get(key, []) + [s]
        return list(m.values())