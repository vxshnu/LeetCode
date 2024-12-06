class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0,x+1):
            if x<i*i:
                return i-1
            elif x == i*i:
                return i
        