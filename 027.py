class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < len(nums):
            if i < 0:
                i = 0
                continue
            if nums[i] == val:
                nums.pop(i)
                k = k-1
                i = i-1
            else:
                i = i+1
        return k