class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        i = 0
        for i in range(1, (x // 2) + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
        return i