class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case 0
        if n < 1:
            return 0
        # Base case 1: n = 1 -> {1}
        if n == 1:
            return 1
        # Base case 2: n = 2 -> {1+1, 2}
        if n == 2:
            return 2
        # Recusrsive case: n > 2
        elif n > 2:
            # At each step you have the choice to take away 1 or 2
            left = self.climbStairs(n-1)
            right = self.climbStairs(n-2)
            return left + right
        