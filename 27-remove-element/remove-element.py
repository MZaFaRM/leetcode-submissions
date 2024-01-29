class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        try:
            while True:
                if nums[i] == val:
                    nums.pop(i)
                else:
                    k += 1
                    i += 1
        except IndexError as e:
            raise e
        finally:
            return k