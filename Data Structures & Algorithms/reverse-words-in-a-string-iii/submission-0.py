class Solution:
    def reverseWords(self, s: str) -> str:
        spl_s = s.split()
        w = ''

        for word in spl_s:
            reversed_word = ''
            for char in word:
                reversed_word = char + reversed_word

            w = w + ''.join(reversed_word) + ' '
        
        return w.strip()
