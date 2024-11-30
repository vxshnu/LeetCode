class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = haystack.find(needle)
        if x != -1:
            return x
        else:
            return -1