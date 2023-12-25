class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        res1 = ''
        res2 = ''
        for i in word1:
            res1 += i
        for i in word2:
            res2 += i

        if res1 == res2:
            return True
        return False

a = Solution()
print(a.arrayStringsAreEqual(["ab", "c"],["a", "cb"]))