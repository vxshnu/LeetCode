class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #solution 1

        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        #solution 2

        unique = set(nums)
        return len(nums) != len(unique)