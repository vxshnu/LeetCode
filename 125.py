class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        l = len(s)-1
        s = s.lower()
        while i < l/2:
            if s[i].isalnum() and s[l-i].isalnum():
                if s[i] != s[l-i]:
                    return False
                print(s[i],s[l-i])
                i = i+1
            else:
                if not s[i].isalnum():
                    s = s[:i] + s[i+1:]
                else:
                    index_to_remove = l - i
                    s = s[:index_to_remove] + s[index_to_remove+1:]
                l = len(s)-1
        return True