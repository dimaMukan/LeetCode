class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res1 = ''
        res = []
        for i in range(len(indices)):
            res.append('')
        r = 0

        for i in indices:
            res[i] = s[r]
            r += 1

        for i in res:
            res1 += i
        return res1

a = Solution()
print(a.restoreString("codeleet",[4,5,6,7,0,2,1,3]))