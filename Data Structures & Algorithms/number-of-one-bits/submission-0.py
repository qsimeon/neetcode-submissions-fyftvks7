class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            bitmask = 1 << i
            total += bool(bitmask & n)
        return total
        