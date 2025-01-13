# 3223. Minimum Length of String After Operations
from collections import Counter

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)
        output = 0
        
        for values in s_counter.values():
            while values > 2:
                values = values - 2
            if values <= 2:
                output += values
        return output
        
        
s = "aa"
sol = Solution()
print(sol.minimumLength(s))