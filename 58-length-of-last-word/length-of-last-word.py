class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        s = ' ' + s
        while s[i] == ' ':
            i -= 1
        n = 0
        while s[i] != ' ':
            i -= 1
            n += 1
        return n