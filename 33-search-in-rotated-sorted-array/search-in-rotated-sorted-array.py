class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = nums.index(target) if target in nums else -1
        return index
        