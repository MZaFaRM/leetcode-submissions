class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0; j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = list(s)
        while i < j:
            while (s[i].lower() not in vowels) and i < j:
                i += 1
            while (s[j].lower() not in vowels) and i < j:
                j -= 1
            if i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
        return ''.join(word)

        