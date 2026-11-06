class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in freqMap:
                freqMap[key].append(word)
                
            else:
                freqMap[key] = [word]
                
        return list(freqMap.values())