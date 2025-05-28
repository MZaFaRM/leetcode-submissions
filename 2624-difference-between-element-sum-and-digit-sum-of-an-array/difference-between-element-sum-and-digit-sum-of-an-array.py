class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = 0
        digi_sum = 0
        for num in nums:
            elem_sum += num
            while num > 0:
                digi_sum += num % 10
                num = num // 10
        return abs(elem_sum - digi_sum)