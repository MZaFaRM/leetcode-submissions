class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        bed_len = len(flowerbed)
        i = 0

        while (i < bed_len) and (n > 0):
            if flowerbed[i] == 1:
                i += 2
                continue
            elif i > 0 and flowerbed[i-1] == 1:
                i += 1
                continue
            elif i + 1 < bed_len and flowerbed[i+1] == 1:
                i += 1
                continue
            else:
                i += 2
                n -= 1
        return n <= 0
        