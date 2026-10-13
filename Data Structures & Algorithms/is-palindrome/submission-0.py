class Solution:
    def isPalindrome(self, s: str) -> bool:
       x = "".join([char for char in s.lower() if char.isalnum()]) 

       l, r = 0, len(x)-1

       while l<r:
        if x[l] != x[r]:
            return False
        l+=1
        r-=1
        
       return True


    