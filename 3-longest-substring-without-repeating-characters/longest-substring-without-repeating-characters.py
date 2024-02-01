class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        seen = []
        max_len = 0

        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.pop(0)
                    j += 1
            seen.append(s[i])
            max_len = max(max_len, i - j + 1)

        return max_len