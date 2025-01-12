class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for a, b in zip(s, s[1:]):
            if symbols[a] < symbols[b]:
                result -= symbols[a]
            else:
                result += symbols[a]
        return result 
    
x = "LVIII"
sol = Solution()
print(sol.romanToInt(x))