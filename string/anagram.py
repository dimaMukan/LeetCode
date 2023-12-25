class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        arr = []
        res = 0
        for i in s:
            arr.append(i)
        for i in t:
            if i in arr:
                arr.remove(i)
            else:
                res += 1
        return res

a = Solution()
print(a.minSteps("bab","abb"))