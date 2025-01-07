class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = set()
        word_len = len(words)
        for i in range(word_len):
            for j in range(word_len):
                if i != j:
                    if words[i] in words[j]:
                        results.add(words[i])
                        break
        
        return list(results)
        

# Example usage:
words = ["mass", "as", "superhero", "hero"]
sol = Solution()
print(sol.stringMatching(words))