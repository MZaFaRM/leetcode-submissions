class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = nums[0]
        k = 1
        temp = nums[1:]
        for i in temp:
            if i != current:
                current = i
                k += 1
            else:
                nums.remove(i)
        return k