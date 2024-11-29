class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        total = 0
        while(i<len(s)):
            value1 = romans[s[i]]
            if i+1 < len(s):
                value2 = romans[s[i+1]]
                if value2 > value1:
                    total = total + value2 - value1
                    i = i+1
                else:
                    total = total + value1
            else:
                total = total + value1
            i = i+1
        return total
        pass