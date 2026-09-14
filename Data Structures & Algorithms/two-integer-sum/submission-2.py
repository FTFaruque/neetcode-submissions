class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}
        
        for i in range(len(nums)):
            prevMap[nums[i]] = i

        for num in nums:
            diff = target - num
            if diff in prevMap and prevMap[diff] != nums.index(num):
                return [nums.index(num), prevMap[diff]]
