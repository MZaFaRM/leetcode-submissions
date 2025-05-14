from math import ceil

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        for i in range(0, ceil(x / 2) + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
        return i