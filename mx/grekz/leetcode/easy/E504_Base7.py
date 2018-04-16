'''
@author: grekz
'''
class E504_Base7:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)