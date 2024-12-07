class Solution:
    def number_to_letter(self, n):
        if 1 <= n <= 26:
            return chr(n + 64)  

    def convertToTitle(self, columnNumber: int) -> str:
        x = columnNumber 
        output = ""
        while x > 0:
            x = x - 1
            r = x % 26
            output = chr(ord('A') + r) + output
            x = x//26
        return output