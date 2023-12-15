class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        plus = ['++X','X++']
        minus = ['--X','X--']
        res = 0
        for i in operations:
            if i in plus:
                res += 1
            if i in minus:
                res -= 1
        return res

a = Solution()
print(a.finalValueAfterOperations(["X++","++X","--X","X--"]))