class Solution(object):
    def computeLPSArray(self, pat, lps):
        M = len(pat)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        lps[0] = 0  # lps[0] is always 0

        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    def KMPSearch(self, pat, txt):
        M = len(pat)
        N = len(txt)
        lps = [0] * M
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(pat, lps)

        i = 0  # index for txt[]
        results = []
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                results.append(i - j)
                j = lps[j - 1]

            elif i < N and pat[j] != txt[i]:  # mismatch after j matches
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return results

    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        found_words = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self.KMPSearch(words[i], words[j]):
                    found_words.append(words[i])
                    break
        return list(set(found_words))

# Example usage:
words = ["mass", "as", "superhero", "hero"]
sol = Solution()
print(sol.stringMatching(words))
