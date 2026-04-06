class Solution:
    def countBits(self, n: int) -> List[int]:
        ## Iterative solution O(nlogn)
        # counts = []
        # res = ''
        # for i in range(n+1):
        #     c = 0
        #     # e.g. i = 1011
        #     while i > 0:
        #         # get least significant (rightmost) bit
        #         c += i & 1 # equivalent to i % 2
        #         # right shift: i=1011 -> i=0101
        #         i = i >> 1 # equivalent to 1 // 2
        #         # repeat until 0010->0001->0000
        #     counts.append(c)
        # return counts

        ## Iterative solution O(n)
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
                

        