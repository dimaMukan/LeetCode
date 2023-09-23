from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(1,len(strs)):
            temp = strs[i]
            index = 0
            res = ''
            while index<len(strs[0]) and index<len(strs[i]):
                if a[index] == temp[index]:
                    res += a[index]
                    index += 1
                else:
                    break
            a = res + ' '
        return a



list = ['akshat', 'akash', 'akshay', 'akshita']
a = Solution()
print(a.longestCommonPrefix(list))
