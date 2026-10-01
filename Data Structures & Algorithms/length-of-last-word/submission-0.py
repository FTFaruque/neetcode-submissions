class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        output = s.split()

        return len(output[-1])