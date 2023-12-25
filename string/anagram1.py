class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        arr = []
        arr1 = []
        items_1 = {}
        items_2 = {}
        res = 0
        for i in s:
            arr.append(i)
            if i in arr:
                items_1[i] = s.count(i)
            else:
                ...

        for i in t:
            arr1.append(i)
            if i not in arr1:
                res += 1



a = Solution()
print(a.minSteps("bab","abb"))