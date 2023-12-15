class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        arr = []
        res = 0
        for i in jewels:
            arr.append(i)
        for i in arr:
            res += stones.count(i)
        return res

a = Solution()
print(a.numJewelsInStones('a','aaAAsss'))
