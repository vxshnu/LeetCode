class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            m = str(x)
            for i in range(0,len(m)):
                if m[i] != m[len(m)-1-i]:
                    return False
            return True