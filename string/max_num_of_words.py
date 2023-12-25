class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        temp = 0
        for i in sentences:
            a = i.split(' ')
            if len(a) > temp:
                temp = len(a)
        return temp

a = Solution()
print(a.mostWordsFound(["a a a","a a aa a"]))