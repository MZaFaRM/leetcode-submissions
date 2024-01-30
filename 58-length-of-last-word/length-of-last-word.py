import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        match = re.search("(\w+) *$", s)
        if match:
            return len(match[1])