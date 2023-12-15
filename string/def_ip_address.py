class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')

a = Solution()
print(a.defangIPaddr('1.1.1.1'))