class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        s = 0
        for i in words:
            if x in i:
                res.append(s)
            s += 1
        return res

a = Solution()
print(a.findWordsContaining(["abc","bcd","aaaa","cbc"],"a"))