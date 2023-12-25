class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        temp_r = 0
        temp_l = 0
        for i in s:
            if i.lower() == 'r':
                temp_r += 1
            if i.lower() == 'l':
                temp_l += 1
            if temp_r == temp_l and temp_l > 0:
                res += 1
                temp_r = 0
                temp_l = 0
        return res

a = Solution()
print(a.balancedStringSplit("lllrrrlrrl"))