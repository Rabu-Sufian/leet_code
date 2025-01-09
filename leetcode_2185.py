# 2185. Counting Words With a Given Prefix

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        pref_len = len(pref)
        for word in words:
            if word[:pref_len] == pref:
                count += 1
        return count
        
# Example usage:
words = ["leetcode","win","loops","success"]
pref = "code"
sol = Solution()
print(sol.prefixCount(words, pref))