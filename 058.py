class Solution:
    def lengthOfLastWord(self, s: str) -> int:      
        s = s.strip()
        l = len(s)-1
        while l >= 0:
            if s[l] == ' ':
                return len(s)-l-1
            l = l-1
        return len(s)