class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        x1 = self.climbStairs(n-1)
        x2 = self.climbStairs(n-2)
        return x1+x2