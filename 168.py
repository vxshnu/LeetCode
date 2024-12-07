class Solution:
    def number_to_letter(self, n):
        if 1 <= n <= 26:
            return chr(n + 64)  

    def convertToTitle(self, columnNumber: int) -> str:
        x = columnNumber // 26
        y = columnNumber % 26
        z = x
        firstalpha = ""
        while z > 0:
            r = z % 26
            if r == 0:  
                firstalpha = self.number_to_letter(26) + firstalpha
                z = (z // 26) - 1 
            else:
                firstalpha = self.number_to_letter(r) + firstalpha
                z = z // 26
            z = z//26
        
        lastalpha = self.number_to_letter(y)
        converted = firstalpha+lastalpha
        return converted
