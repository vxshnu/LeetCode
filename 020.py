class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[',')':'(','}':'{'}
        lastopened = ['$']
        for i in range(0,len(s)):   
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                lastopened.append(s[i])
            elif lastopened[len(lastopened)-1] == brackets[s[i]]:
                lastopened.pop()
            else:
                return False
        if len(lastopened) == 1:
            return True
        else:
            return False
