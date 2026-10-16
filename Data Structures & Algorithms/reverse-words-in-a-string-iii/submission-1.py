class Solution:
    def reverseWords(self, s: str) -> str:
        spl_s = s.split()
        w = ''

        # for word in spl_s:
        #     reversed_word = ''
        #     for char in word:
        #         reversed_word = char + reversed_word

        #     w = w + ''.join(reversed_word) + ' '
        
        # l = 0 
        # r = len(spl_s[l]) - 1

        for l in range(len(spl_s)):
            for r in range(len(spl_s[l])-1, -1, -1):
                w = w + ''.join(spl_s[l][r]) 
            w = w + ' '
    
        return w.strip()
