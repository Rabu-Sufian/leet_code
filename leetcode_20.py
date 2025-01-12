class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif stack:  
                if (p == ')' and stack[-1] == '(') or \
                   (p == '}' and stack[-1] == '{') or \
                   (p == ']' and stack[-1] == '['):
                    stack.pop()  
                else:
                    return False
            else:
                return False
            
        return not stack
        
s = "[([]])"
sol = Solution()
print(sol.isValid(s))