class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits.pop()
        last += 1
        zeroes = 0
        while digits and last >= 10:
            zeroes += 1
            last = digits.pop()
            last += 1
        if last >= 10:
            digits.append(1)
            zeroes += 1
        else:
            digits.append(last)

        digits.extend([0] * zeroes)
        return digits
