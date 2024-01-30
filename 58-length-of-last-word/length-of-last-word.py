class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        match = s.strip().split(' ')[-1]
        return len(match)