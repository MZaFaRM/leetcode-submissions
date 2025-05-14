from math import ceil

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = ceil(x / 2)
        while low <= high:
            mid = (high + low) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1