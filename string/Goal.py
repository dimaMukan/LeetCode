class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ''
        for i in range(len(command)):
            if command[i].upper() == 'G':
                res += '(G)'
            elif command[i].upper() == 'O':
                res += '()'
            elif command[i].upper() == 'A' and command[i+1].upper() == 'L':
                res += '(al)'
        return res

a = Solution()
print(a.interpret('lalgoal'))
