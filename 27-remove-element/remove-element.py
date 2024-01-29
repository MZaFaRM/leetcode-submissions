class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        k = 0
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            else:
                k += 1
            i -= 1
        return k