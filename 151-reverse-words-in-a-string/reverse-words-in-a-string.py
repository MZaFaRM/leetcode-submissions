class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        cleaned = [word for word in words if word]
        cleaned.reverse()
        return " ".join(cleaned)