class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len(word1):
            return merged + word1[i:]
        elif j < len(word2):
            return merged + word2[j:]
        return merged