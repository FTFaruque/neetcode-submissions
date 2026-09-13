class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j_value = target - nums[i]
            j = i + 1
            while j < len(nums):
                if nums[j] == j_value:
                    return [i, j]
                j += 1
