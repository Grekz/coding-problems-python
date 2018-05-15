'''
@author: grekz
'''
class E551_StudentAttendanceRecordI:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "LLL" not in s and s.find("A") == s.rfind("A")        