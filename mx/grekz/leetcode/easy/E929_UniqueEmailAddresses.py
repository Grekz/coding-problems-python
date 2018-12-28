'''
@author: grekz
'''
class E929_UniqueEmailAddresses:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        for e in emails:
            parts = re.split(r'[+@]', e)
            a = parts[0].replace(".", "")
            s.add(a + parts[-1])
        return len(s)