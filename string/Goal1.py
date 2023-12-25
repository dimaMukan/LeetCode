class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace('()','o')
        command = command.replace('(al)','al')
        return command

a = Solution()
print(a.interpret('G()(al)'))
