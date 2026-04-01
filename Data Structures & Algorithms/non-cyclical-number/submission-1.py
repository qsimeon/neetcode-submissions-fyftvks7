class Solution:
    def isHappy(self, n: int) -> bool:
        # init  = n
        # while True:
        #     # the sum of the squares of its digits
        #     sumOfSquares = sum(int(i)**2 for i in str(n)) 
        #     # if it stops at 1 it is a non-cyclical number
        #     if sumOfSquares == 1:
        #         return True 
        #     n = sumOfSquares
        #     # loops in a cycle
        #     if n == init or len(str(n)) == 1:
        #         return False
        
        def sumOfSquares(n: int):
            return sum(int(i)**2 for i in str(n))

        seen = {n}
        while True:
            n = sumOfSquares(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)

        