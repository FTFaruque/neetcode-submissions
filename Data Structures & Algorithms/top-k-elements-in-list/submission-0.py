class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        sorted_keys = sorted(freqMap.keys(), 
                            key=lambda x: freqMap[x], 
                            reverse=True)
        
        return sorted_keys[:k]