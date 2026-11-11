class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_seen = 0, 0

        for num in nums:
            if num == 1:
                count += 1
                if count > max_seen:
                    max_seen = count
            else:
                count = 0

        return max_seen
                