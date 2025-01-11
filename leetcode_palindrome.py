class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_s = str(x)
        is_valid = False
        print(x_s)
       
        if all(x_s[i] == x_s[-(i+1)] for i in range(len(x_s))):
            is_valid = True
        return is_valid
x = 1000021
sol = Solution()
print(sol.isPalindrome(x))