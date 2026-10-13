class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r  = 0, len(s)-1
        temp = ''
        while l<r:
            # s[l], s[r] = s[r], s[l]
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1
        
        
        
 


        