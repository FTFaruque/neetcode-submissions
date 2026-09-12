class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = dict()
        t_hashmap = dict()

        for ch in s:
            if ch in s_hashmap:    
                s_hashmap[ch] += 1
            else:
                s_hashmap[ch] = 1

        for ch in t:
            if ch in t_hashmap:    
                t_hashmap[ch] += 1
            else:
                t_hashmap[ch] = 1

        if s_hashmap == t_hashmap:
            return True
        
        return False