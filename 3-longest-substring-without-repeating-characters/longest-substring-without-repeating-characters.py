class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        longest_len = 0
        
        for letter in s:
            i = 0
            n = len(substrings)
            while i < n:
                if letter in substrings[i]:
                    string = substrings.pop(i)
                    if (length := len(string)) > longest_len: 
                        longest_len = length
                    n -= 1
                    
                else:
                    substrings[i] += letter
                    i += 1

            substrings.append(letter)
        if substrings:
            longest_len = max(longest_len, len(max(substrings, key=len)))

        return longest_len