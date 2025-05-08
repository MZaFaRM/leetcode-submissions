class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        n = len(haystack)
        m = len(needle)
        limit = n - m
        start = -1
        while i <= limit:
            if haystack[i] == needle[j]:
                start = i
                while j < m and haystack[i] == needle[j]:
                    j += 1
                    i += 1
                if j == m:
                    return start
                else:
                    j = 0
                    i = start
            i += 1
        return -1