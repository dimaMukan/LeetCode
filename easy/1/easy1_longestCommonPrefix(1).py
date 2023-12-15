import os
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = os.path.commonprefix(strs)
        return prefix

list = ['akshat', 'akash', 'akshay', 'akshita']
a = Solution()
print(a.longestCommonPrefix(list))