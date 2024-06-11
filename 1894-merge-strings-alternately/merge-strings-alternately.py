class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        while word1 and word2:
            merged += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        return merged + word1 + word2